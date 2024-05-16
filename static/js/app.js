"use strict";

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

/**
 * This library was created to emulate some jQuery features
 * used in this template only with Javascript and DOM
 * manipulation functions (IE10+).
 * All methods were designed for an adequate and specific use
 * and don't perform a deep validation on the arguments provided.
 *
 * IMPORTANT:
 * ==========
 * It's suggested NOT to use this library extensively unless you
 * understand what each method does. Instead, use only JS or
 * you might even need jQuery.
 */
(function (global, factory) {
  if ((typeof exports === "undefined" ? "undefined" : _typeof(exports)) === 'object') {
    // CommonJS-like
    module.exports = factory();
  } else {
    // Browser
    if (typeof global.jQuery === 'undefined') global.$ = factory();
  }
})(window, function () {
  // HELPERS
  function arrayFrom(obj) {
    return 'length' in obj && obj !== window ? [].slice.call(obj) : [obj];
  }

  function _filter(ctx, fn) {
    return [].filter.call(ctx, fn);
  }

  function map(ctx, fn) {
    return [].map.call(ctx, fn);
  }

  function matches(item, selector) {
    return (Element.prototype.matches || Element.prototype.msMatchesSelector).call(item, selector);
  } // Events handler with simple scoped events support


  var EventHandler = function EventHandler() {
    this.events = {};
  };

  EventHandler.prototype = {
    // event accepts: 'click' or 'click.scope'
    bind: function bind(event, listener, target) {
      var type = event.split('.')[0];
      target.addEventListener(type, listener, false);
      this.events[event] = {
        type: type,
        listener: listener
      };
    },
    unbind: function unbind(event, target) {
      if (event in this.events) {
        target.removeEventListener(this.events[event].type, this.events[event].listener, false);
        delete this.events[event];
      }
    }
  }; // Object Definition

  var Wrap = function Wrap(selector) {
    this.selector = selector;
    return this._setup([]);
  }; // CONSTRUCTOR


  Wrap.Constructor = function (param, attrs) {
    var el = new Wrap(param);
    return el.init(attrs);
  }; // Core methods


  Wrap.prototype = {
    constructor: Wrap,

    /**
     * Initialize the object depending on param type
     * [attrs] only to handle $(htmlString, {attributes})
     */
    init: function init(attrs) {
      // empty object
      if (!this.selector) return this; // selector === string

      if (typeof this.selector === 'string') {
        // if looks like markup, try to create an element
        if (this.selector[0] === '<') {
          var elem = this._setup([this._create(this.selector)]);

          return attrs ? elem.attr(attrs) : elem;
        } else return this._setup(arrayFrom(document.querySelectorAll(this.selector)));
      } // selector === DOMElement


      if (this.selector.nodeType) return this._setup([this.selector]);else // shorthand for DOMReady
        if (typeof this.selector === 'function') return this._setup([document]).ready(this.selector); // Array like objects (e.g. NodeList/HTMLCollection)

      return this._setup(arrayFrom(this.selector));
    },

    /**
     * Creates a DOM element from a string
     * Strictly supports the form: '<tag>' or '<tag/>'
     */
    _create: function _create(str) {
      var nodeName = str.substr(str.indexOf('<') + 1, str.indexOf('>') - 1).replace('/', '');
      return document.createElement(nodeName);
    },

    /** setup properties and array to element set */
    _setup: function _setup(elements) {
      var i = 0;

      for (; i < elements.length; i++) {
        delete this[i];
      } // clean up old set


      this.elements = elements;
      this.length = elements.length;

      for (i = 0; i < elements.length; i++) {
        this[i] = elements[i];
      } // new set


      return this;
    },
    _first: function _first(cb, ret) {
      var f = this.elements[0];
      return f ? cb ? cb.call(this, f) : f : ret;
    },

    /** Common function for class manipulation  */
    _classes: function _classes(method, classname) {
      var cls = classname.split(' ');

      if (cls.length > 1) {
        cls.forEach(this._classes.bind(this, method));
      } else {
        if (method === 'contains') {
          var elem = this._first();

          return elem ? elem.classList.contains(classname) : false;
        }

        return classname === '' ? this : this.each(function (i, item) {
          item.classList[method](classname);
        });
      }
    },

    /**
     * Multi purpose function to set or get a (key, value)
     * If no value, works as a getter for the given key
     * key can be an object in the form {key: value, ...}
     */
    _access: function _access(key, value, fn) {
      if (_typeof(key) === 'object') {
        for (var k in key) {
          this._access(k, key[k], fn);
        }
      } else if (value === undefined) {
        return this._first(function (elem) {
          return fn(elem, key);
        });
      }

      return this.each(function (i, item) {
        fn(item, key, value);
      });
    },
    each: function each(fn, arr) {
      arr = arr ? arr : this.elements;

      for (var i = 0; i < arr.length; i++) {
        if (fn.call(arr[i], i, arr[i]) === false) break;
      }

      return this;
    }
  };
  /** Allows to extend with new methods */

  Wrap.extend = function (methods) {
    Object.keys(methods).forEach(function (m) {
      Wrap.prototype[m] = methods[m];
    });
  }; // DOM READY


  Wrap.extend({
    ready: function ready(fn) {
      if (document.attachEvent ? document.readyState === 'complete' : document.readyState !== 'loading') {
        fn();
      } else {
        document.addEventListener('DOMContentLoaded', fn);
      }

      return this;
    }
  }); // ACCESS

  Wrap.extend({
    /** Get or set a css value */
    css: function css(key, value) {
      var getStyle = function getStyle(e, k) {
        return e.style[k] || getComputedStyle(e)[k];
      };

      return this._access(key, value, function (item, k, val) {
        var unit = typeof val === 'number' ? 'px' : '';
        return val === undefined ? getStyle(item, k) : item.style[k] = val + unit;
      });
    },

    /** Get an attribute or set it */
    attr: function attr(key, value) {
      return this._access(key, value, function (item, k, val) {
        return val === undefined ? item.getAttribute(k) : item.setAttribute(k, val);
      });
    },

    /** Get a property or set it */
    prop: function prop(key, value) {
      return this._access(key, value, function (item, k, val) {
        return val === undefined ? item[k] : item[k] = val;
      });
    },
    position: function position() {
      return this._first(function (elem) {
        return {
          left: elem.offsetLeft,
          top: elem.offsetTop
        };
      });
    },
    scrollTop: function scrollTop(value) {
      return this._access('scrollTop', value, function (item, k, val) {
        return val === undefined ? item[k] : item[k] = val;
      });
    },
    outerHeight: function outerHeight(includeMargin) {
      return this._first(function (elem) {
        var style = getComputedStyle(elem);
        var margins = includeMargin ? parseInt(style.marginTop, 10) + parseInt(style.marginBottom, 10) : 0;
        return elem.offsetHeight + margins;
      });
    },

    /**
     * Find the position of the first element in the set
     * relative to its sibling elements.
     */
    index: function index() {
      return this._first(function (el) {
        return arrayFrom(el.parentNode.children).indexOf(el);
      }, -1);
    }
  }); // LOOKUP

  Wrap.extend({
    children: function children(selector) {
      var childs = [];
      this.each(function (i, item) {
        childs = childs.concat(map(item.children, function (item) {
          return item;
        }));
      });
      return Wrap.Constructor(childs).filter(selector);
    },
    siblings: function siblings() {
      var sibs = [];
      this.each(function (i, item) {
        sibs = sibs.concat(_filter(item.parentNode.children, function (child) {
          return child !== item;
        }));
      });
      return Wrap.Constructor(sibs);
    },

    /** Return the parent of each element in the current set */
    parent: function parent() {
      var par = map(this.elements, function (item) {
        return item.parentNode;
      });
      return Wrap.Constructor(par);
    },

    /** Return ALL parents of each element in the current set */
    parents: function parents(selector) {
      var par = [];
      this.each(function (i, item) {
        for (var p = item.parentElement; p; p = p.parentElement) {
          par.push(p);
        }
      });
      return Wrap.Constructor(par).filter(selector);
    },

    /**
     * Get the descendants of each element in the set, filtered by a selector
     * Selector can't start with ">" (:scope not supported on IE).
     */
    find: function find(selector) {
      var found = [];
      this.each(function (i, item) {
        found = found.concat(map(item.querySelectorAll(
        /*':scope ' + */
        selector), function (fitem) {
          return fitem;
        }));
      });
      return Wrap.Constructor(found);
    },

    /** filter the actual set based on given selector */
    filter: function filter(selector) {
      if (!selector) return this;

      var res = _filter(this.elements, function (item) {
        return matches(item, selector);
      });

      return Wrap.Constructor(res);
    },

    /** Works only with a string selector */
    is: function is(selector) {
      var found = false;
      this.each(function (i, item) {
        return !(found = matches(item, selector));
      });
      return found;
    }
  }); // ELEMENTS

  Wrap.extend({
    /**
     * append current set to given node
     * expects a dom node or set
     * if element is a set, prepends only the first
     */
    appendTo: function appendTo(elem) {
      elem = elem.nodeType ? elem : elem._first();
      return this.each(function (i, item) {
        elem.appendChild(item);
      });
    },

    /**
     * Append a domNode to each element in the set
     * if element is a set, append only the first
     */
    append: function append(elem) {
      elem = elem.nodeType ? elem : elem._first();
      return this.each(function (i, item) {
        item.appendChild(elem);
      });
    },

    /**
     * Insert the current set of elements after the element
     * that matches the given selector in param
     */
    insertAfter: function insertAfter(selector) {
      var target = document.querySelector(selector);
      return this.each(function (i, item) {
        target.parentNode.insertBefore(item, target.nextSibling);
      });
    },

    /**
     * Clones all element in the set
     * returns a new set with the cloned elements
     */
    clone: function clone() {
      var clones = map(this.elements, function (item) {
        return item.cloneNode(true);
      });
      return Wrap.Constructor(clones);
    },

    /** Remove all node in the set from DOM. */
    remove: function remove() {
      this.each(function (i, item) {
        delete item.events;
        delete item.data;
        if (item.parentNode) item.parentNode.removeChild(item);
      });

      this._setup([]);
    }
  }); // DATASETS

  Wrap.extend({
    /**
     * Expected key in camelCase format
     * if value provided save data into element set
     * if not, return data for the first element
     */
    data: function data(key, value) {
      var hasJSON = /^(?:\{[\w\W]*\}|\[[\w\W]*\])$/,
          dataAttr = 'data-' + key.replace(/[A-Z]/g, '-$&').toLowerCase();

      if (value === undefined) {
        return this._first(function (el) {
          if (el.data && el.data[key]) return el.data[key];else {
            var data = el.getAttribute(dataAttr);
            if (data === 'true') return true;
            if (data === 'false') return false;
            if (data === +data + '') return +data;
            if (hasJSON.test(data)) return JSON.parse(data);
            return data;
          }
        });
      } else {
        return this.each(function (i, item) {
          item.data = item.data || {};
          item.data[key] = value;
        });
      }
    }
  }); // EVENTS

  Wrap.extend({
    trigger: function trigger(type) {
      type = type.split('.')[0]; // ignore namespace

      var event = document.createEvent('HTMLEvents');
      event.initEvent(type, true, false);
      return this.each(function (i, item) {
        item.dispatchEvent(event);
      });
    },
    blur: function blur() {
      return this.trigger('blur');
    },
    focus: function focus() {
      return this.trigger('focus');
    },
    on: function on(event, callback) {
      return this.each(function (i, item) {
        if (!item.events) item.events = new EventHandler();
        event.split(' ').forEach(function (ev) {
          item.events.bind(ev, callback, item);
        });
      });
    },
    off: function off(event) {
      return this.each(function (i, item) {
        if (item.events) {
          item.events.unbind(event, item);
          delete item.events;
        }
      });
    }
  }); // CLASSES

  Wrap.extend({
    toggleClass: function toggleClass(classname) {
      return this._classes('toggle', classname);
    },
    addClass: function addClass(classname) {
      return this._classes('add', classname);
    },
    removeClass: function removeClass(classname) {
      return this._classes('remove', classname);
    },
    hasClass: function hasClass(classname) {
      return this._classes('contains', classname);
    }
  });
  /**
   * Some basic features in this template relies on Bootstrap
   * plugins, like Collapse, Dropdown and Tab.
   * Below code emulates plugins behavior by toggling classes
   * from elements to allow a minimum interaction without animation.
   * - Only Collapse is required which is used by the sidebar.
   * - Tab and Dropdown are optional features.
   */
  // Emulate jQuery symbol to simplify usage

  var $ = Wrap.Constructor; // Emulates Collapse plugin

  Wrap.extend({
    collapse: function collapse(action) {
      return this.each(function (i, item) {
        var $item = $(item).trigger(action + '.bs.collapse');
        if (action === 'toggle') $item.collapse($item.hasClass('show') ? 'hide' : 'show');else $item[action === 'show' ? 'addClass' : 'removeClass']('show');
      });
    }
  }); // Initializations

  $('[data-toggle]').on('click', function (e) {
    var target = $(e.currentTarget);
    if (target.is('a')) e.preventDefault();

    switch (target.data('toggle')) {
      case 'collapse':
        $(target.attr('href')).collapse('toggle');
        break;

      case 'tab':
        target.parent().parent().find('.active').removeClass('active');
        target.addClass('active');
        var tabPane = $(target.attr('href'));
        tabPane.siblings().removeClass('active show');
        tabPane.addClass('active show');
        break;

      case 'dropdown':
        var dd = target.parent().toggleClass('show');
        dd.find('.dropdown-menu').toggleClass('show');
        break;

      default:
        break;
    }
  });
  return Wrap.Constructor;
});
/*!
 *
 * Angle - Bootstrap Admin Template
 *
 * Version: 4.8.1
 * Author: @themicon_co
 * Website: http://themicon.co
 * License: https://wrapbootstrap.com/help/licenses
 *
 */


(function () {
  'use strict';

  $(function () {
    // Restore body classes
    // -----------------------------------
    var $body = $('body');
    new StateToggler().restoreState($body); // enable settings toggle after restore

    $('#chk-fixed').prop('checked', $body.hasClass('layout-fixed'));
    $('#chk-collapsed').prop('checked', $body.hasClass('aside-collapsed'));
    $('#chk-collapsed-text').prop('checked', $body.hasClass('aside-collapsed-text'));
    $('#chk-boxed').prop('checked', $body.hasClass('layout-boxed'));
    $('#chk-float').prop('checked', $body.hasClass('aside-float'));
    $('#chk-hover').prop('checked', $body.hasClass('aside-hover')); // When ready display the offsidebar

    $('.offsidebar.d-none').removeClass('d-none'); // DEMO ONLY: remove sidebar related classes as they dont
    // have effect with horizontal layout and disabled switches

    if (document.body.className.indexOf('layout-h') > -1) {
      document.body.className = document.body.className.replace(/(^|\s)aside-\S+/g, '');
      $('#chk-collapsed').prop({
        disabled: true,
        checked: false
      });
      $('#chk-collapsed-text').prop({
        disabled: true,
        checked: false
      });
      $('#chk-float').prop({
        disabled: true,
        checked: false
      });
      $('#chk-hover').prop({
        disabled: true,
        checked: false
      });
      $('#chk-scroll').prop({
        disabled: true,
        checked: false
      });
    }
  }); // doc ready
})(); // Start Bootstrap JS
// -----------------------------------


(function () {
  'use strict';

  $(initBootstrap);

  function initBootstrap() {
    // necessary check at least til BS doesn't require jQuery
    if (!$.fn || !$.fn.tooltip || !$.fn.popover) return; // POPOVER
    // -----------------------------------

    $('[data-toggle="popover"]').popover(); // TOOLTIP
    // -----------------------------------

    $('[data-toggle="tooltip"]').tooltip({
      container: 'body'
    }); // DROPDOWN INPUTS
    // -----------------------------------

    $('.dropdown input').on('click focus', function (event) {
      event.stopPropagation();
    });
  }
})(); // Module: card-tools
// -----------------------------------


(function () {
  'use strict';

  $(initCardDismiss);
  $(initCardCollapse);
  $(initCardRefresh);
  /**
   * Helper function to find the closest
   * ascending .card element
   */

  function getCardParent(item) {
    var el = item.parentElement;

    while (el && !el.classList.contains('card')) {
      el = el.parentElement;
    }

    return el;
  }
  /**
   * Helper to trigger custom event
   */


  function triggerEvent(type, item, data) {
    var ev;

    if (typeof CustomEvent === 'function') {
      ev = new CustomEvent(type, {
        detail: data
      });
    } else {
      ev = document.createEvent('CustomEvent');
      ev.initCustomEvent(type, true, false, data);
    }

    item.dispatchEvent(ev);
  }
  /**
   * Dismiss cards
   * [data-tool="card-dismiss"]
   */


  function initCardDismiss() {
    var cardtoolSelector = '[data-tool="card-dismiss"]';
    var cardList = [].slice.call(document.querySelectorAll(cardtoolSelector));
    cardList.forEach(function (item) {
      new CardDismiss(item);
    });

    function CardDismiss(item) {
      var EVENT_REMOVE = 'card.remove';
      var EVENT_REMOVED = 'card.removed';
      this.item = item;
      this.cardParent = getCardParent(this.item);
      this.removing = false; // prevents double execution

      this.clickHandler = function (e) {
        if (this.removing) return;
        this.removing = true; // pass callbacks via event.detail to confirm/cancel the removal

        triggerEvent(EVENT_REMOVE, this.cardParent, {
          confirm: this.confirm.bind(this),
          cancel: this.cancel.bind(this)
        });
      };

      this.confirm = function () {
        this.animate(this.cardParent, function () {
          triggerEvent(EVENT_REMOVED, this.cardParent);
          this.remove(this.cardParent);
        });
      };

      this.cancel = function () {
        this.removing = false;
      };

      this.animate = function (item, cb) {
        if ('onanimationend' in window) {
          // animation supported
          item.addEventListener('animationend', cb.bind(this));
          item.className += ' animated bounceOut'; // requires animate.css
        } else cb.call(this); // no animation, just remove

      };

      this.remove = function (item) {
        item.parentNode.removeChild(item);
      }; // attach listener


      item.addEventListener('click', this.clickHandler.bind(this), false);
    }
  }
  /**
   * Collapsed cards
   * [data-tool="card-collapse"]
   * [data-start-collapsed]
   */


  function initCardCollapse() {
    var cardtoolSelector = '[data-tool="card-collapse"]';
    var cardList = [].slice.call(document.querySelectorAll(cardtoolSelector));
    cardList.forEach(function (item) {
      var initialState = item.hasAttribute('data-start-collapsed');
      new CardCollapse(item, initialState);
    });

    function CardCollapse(item, startCollapsed) {
      var EVENT_SHOW = 'card.collapse.show';
      var EVENT_HIDE = 'card.collapse.hide';
      this.state = true; // true -> show / false -> hide

      this.item = item;
      this.cardParent = getCardParent(this.item);
      this.wrapper = this.cardParent.querySelector('.card-wrapper');

      this.toggleCollapse = function (action) {
        triggerEvent(action ? EVENT_SHOW : EVENT_HIDE, this.cardParent);
        this.wrapper.style.maxHeight = (action ? this.wrapper.scrollHeight : 0) + 'px';
        this.state = action;
        this.updateIcon(action);
      };

      this.updateIcon = function (action) {
        this.item.firstElementChild.className = action ? 'fa fa-minus' : 'fa fa-plus';
      };

      this.clickHandler = function () {
        this.toggleCollapse(!this.state);
      };

      this.initStyles = function () {
        this.wrapper.style.maxHeight = this.wrapper.scrollHeight + 'px';
        this.wrapper.style.transition = 'max-height 0.5s';
        this.wrapper.style.overflow = 'hidden';
      }; // prepare styles for collapse animation


      this.initStyles(); // set initial state if provided

      if (startCollapsed) {
        this.toggleCollapse(false);
      } // attach listener


      this.item.addEventListener('click', this.clickHandler.bind(this), false);
    }
  }
  /**
   * Refresh cards
   * [data-tool="card-refresh"]
   * [data-spinner="standard"]
   */


  function initCardRefresh() {
    var cardtoolSelector = '[data-tool="card-refresh"]';
    var cardList = [].slice.call(document.querySelectorAll(cardtoolSelector));
    cardList.forEach(function (item) {
      new CardRefresh(item);
    });

    function CardRefresh(item) {
      var EVENT_REFRESH = 'card.refresh';
      var WHIRL_CLASS = 'whirl';
      var DEFAULT_SPINNER = 'standard';
      this.item = item;
      this.cardParent = getCardParent(this.item);
      this.spinner = ((this.item.dataset || {}).spinner || DEFAULT_SPINNER).split(' '); // support space separated classes

      this.refresh = function (e) {
        var card = this.cardParent; // start showing the spinner

        this.showSpinner(card, this.spinner); // attach as public method

        card.removeSpinner = this.removeSpinner.bind(this); // Trigger the event and send the card

        triggerEvent(EVENT_REFRESH, card, {
          card: card
        });
      };

      this.showSpinner = function (card, spinner) {
        card.classList.add(WHIRL_CLASS);
        spinner.forEach(function (s) {
          card.classList.add(s);
        });
      };

      this.removeSpinner = function () {
        this.cardParent.classList.remove(WHIRL_CLASS);
      }; // attach listener


      this.item.addEventListener('click', this.refresh.bind(this), false);
    }
  }
})(); // GLOBAL CONSTANTS
// -----------------------------------


(function () {
  window.APP_COLORS = {
    'primary': '#5d9cec',
    'success': '#27c24c',
    'info': '#23b7e5',
    'warning': '#ff902b',
    'danger': '#f05050',
    'inverse': '#131e26',
    'green': '#37bc9b',
    'pink': '#f532e5',
    'purple': '#7266ba',
    'dark': '#3a3f51',
    'yellow': '#fad732',
    'gray-darker': '#232735',
    'gray-dark': '#3a3f51',
    'gray': '#dde6e9',
    'gray-light': '#e4eaec',
    'gray-lighter': '#edf1f2'
  };
  window.APP_MEDIAQUERY = {
    'desktopLG': 1200,
    'desktop': 992,
    'tablet': 768,
    'mobile': 480
  };
})(); // FULLSCREEN
// -----------------------------------


(function () {
  'use strict';

  $(initScreenFull);

  function initScreenFull() {
    if (typeof screenfull === 'undefined') return;
    var $doc = $(document);
    var $fsToggler = $('[data-toggle-fullscreen]'); // Not supported under IE

    var ua = window.navigator.userAgent;

    if (ua.indexOf("MSIE ") > 0 || !!ua.match(/Trident.*rv\:11\./)) {
      $fsToggler.addClass('d-none'); // hide element

      return; // and abort
    }

    $fsToggler.on('click', function (e) {
      e.preventDefault();

      if (screenfull.enabled) {
        screenfull.toggle(); // Switch icon indicator

        toggleFSIcon($fsToggler);
      } else {
        console.log('Fullscreen not enabled');
      }
    });
    if (screenfull.raw && screenfull.raw.fullscreenchange) $doc.on(screenfull.raw.fullscreenchange, function () {
      toggleFSIcon($fsToggler);
    });

    function toggleFSIcon($element) {
      if (screenfull.isFullscreen) $element.children('em').removeClass('fa-expand').addClass('fa-compress');else $element.children('em').removeClass('fa-compress').addClass('fa-expand');
    }
  }
})(); // LOAD CUSTOM CSS
// -----------------------------------


(function () {
  'use strict';

  $(initLoadCSS);

  function initLoadCSS() {
    $('[data-load-css]').on('click', function (e) {
      var element = $(this);
      if (element.is('a')) e.preventDefault();
      var uri = element.data('loadCss'),
          link;

      if (uri) {
        link = createLink(uri);

        if (!link) {
          $.error('Error creating stylesheet link element.');
        }
      } else {
        $.error('No stylesheet location defined.');
      }
    });
  }

  function createLink(uri) {
    var linkId = 'autoloaded-stylesheet',
        oldLink = $('#' + linkId).attr('id', linkId + '-old');
    $('head').append($('<link/>').attr({
      'id': linkId,
      'rel': 'stylesheet',
      'href': uri
    }));

    if (oldLink.length) {
      oldLink.remove();
    }

    return $('#' + linkId);
  }
})(); // TRANSLATION
// -----------------------------------


(function () {
  'use strict';

  $(initTranslation);
  var pathPrefix = 'server/i18n'; // folder of json files

  var STORAGEKEY = 'jq-appLang';
  var savedLanguage = Storages.localStorage.get(STORAGEKEY);

  function initTranslation() {
    i18next.use(i18nextXHRBackend) // .use(LanguageDetector)
    .init({
      fallbackLng: savedLanguage || 'en',
      backend: {
        loadPath: pathPrefix + '/{{ns}}-{{lng}}.json'
      },
      ns: ['site'],
      defaultNS: 'site',
      debug: false
    }, function (err, t) {
      // initialize elements
      applyTranlations(); // listen to language changes

      attachChangeListener();
    });

    function applyTranlations() {
      var list = [].slice.call(document.querySelectorAll('[data-localize]'));
      list.forEach(function (item) {
        var key = item.getAttribute('data-localize');
        if (i18next.exists(key)) item.innerHTML = i18next.t(key);
      });
    }

    function attachChangeListener() {
      var list = [].slice.call(document.querySelectorAll('[data-set-lang]'));
      list.forEach(function (item) {
        item.addEventListener('click', function (e) {
          if (e.target.tagName === 'A') e.preventDefault();
          var lang = item.getAttribute('data-set-lang');

          if (lang) {
            i18next.changeLanguage(lang, function (err) {
              if (err) console.log(err);else {
                applyTranlations();
                Storages.localStorage.set(STORAGEKEY, lang);
              }
            });
          }

          activateDropdown(item);
        });
      });
    }

    function activateDropdown(item) {
      if (item.classList.contains('dropdown-item')) {
        item.parentElement.previousElementSibling.innerHTML = item.innerHTML;
      }
    }
  }
})(); // NAVBAR SEARCH
// -----------------------------------


(function () {
  'use strict';

  $(initNavbarSearch);

  function initNavbarSearch() {
    var navSearch = new navbarSearchInput(); // Open search input

    var $searchOpen = $('[data-search-open]');
    $searchOpen.on('click', function (e) {
      e.stopPropagation();
    }).on('click', navSearch.toggle); // Close search input

    var $searchDismiss = $('[data-search-dismiss]');
    var inputSelector = '.navbar-form input[type="text"]';
    $(inputSelector).on('click', function (e) {
      e.stopPropagation();
    }).on('keyup', function (e) {
      if (e.keyCode == 27) // ESC
        navSearch.dismiss();
    }); // click anywhere closes the search

    $(document).on('click', navSearch.dismiss); // dismissable options

    $searchDismiss.on('click', function (e) {
      e.stopPropagation();
    }).on('click', navSearch.dismiss);
  }

  var navbarSearchInput = function navbarSearchInput() {
    var navbarFormSelector = 'form.navbar-form';
    return {
      toggle: function toggle() {
        var navbarForm = $(navbarFormSelector);
        navbarForm.toggleClass('open');
        var isOpen = navbarForm.hasClass('open');
        navbarForm.find('input')[isOpen ? 'focus' : 'blur']();
      },
      dismiss: function dismiss() {
        $(navbarFormSelector).removeClass('open') // Close control
        .find('input[type="text"]').blur() // remove focus
        // .val('')                    // Empty input
        ;
      }
    };
  };
})(); // NOW TIMER
// -----------------------------------


(function () {
  'use strict';

  $(initNowTimer);

  function initNowTimer() {
    if (typeof moment === 'undefined') return;
    $('[data-now]').each(function () {
      var element = $(this),
          format = element.data('format');

      function updateTime() {
        var dt = moment(new Date()).format(format);
        element.text(dt);
      }

      updateTime();
      setInterval(updateTime, 1000);
    });
  }
})(); // Toggle RTL mode for demo
// -----------------------------------


(function () {
  'use strict';

  $(initRTL);

  function initRTL() {
    var maincss = $('#maincss');
    var bscss = $('#bscss');
    $('#chk-rtl').on('change', function () {
      // app rtl check
      maincss.attr('href', this.checked ? 'css/app-rtl.css' : 'css/app.css'); // bootstrap rtl check

      bscss.attr('href', this.checked ? 'css/bootstrap-rtl.css' : 'css/bootstrap.css');
    });
  }
})(); // SIDEBAR
// -----------------------------------


(function () {
  'use strict';

  $(initSidebar);
  var $html;
  var $body;
  var $sidebar;

  function initSidebar() {
    $html = $('html');
    $body = $('body');
    $sidebar = $('.sidebar'); // AUTOCOLLAPSE ITEMS
    // -----------------------------------

    var sidebarCollapse = $sidebar.find('.collapse');
    sidebarCollapse.on('show.bs.collapse', function (event) {
      event.stopPropagation();
      if ($(this).parents('.collapse').length === 0) sidebarCollapse.filter('.show').collapse('hide');
    }); // SIDEBAR ACTIVE STATE
    // -----------------------------------
    // Find current active item

    var currentItem = $('.sidebar .active').parents('li'); // hover mode don't try to expand active collapse

    if (!useAsideHover()) currentItem.addClass('active') // activate the parent
    .children('.collapse') // find the collapse
    .collapse('show'); // and show it
    // remove this if you use only collapsible sidebar items

    $sidebar.find('li > a + ul').on('show.bs.collapse', function (e) {
      if (useAsideHover()) e.preventDefault();
    }); // SIDEBAR COLLAPSED ITEM HANDLER
    // -----------------------------------

    var eventName = isTouch() ? 'click' : 'mouseenter';
    var subNav = $();
    $sidebar.find('.sidebar-nav > li').on(eventName, function (e) {
      if (isSidebarCollapsed() || useAsideHover()) {
        subNav.trigger('mouseleave');
        subNav = toggleMenuItem($(this)); // Used to detect click and touch events outside the sidebar

        sidebarAddBackdrop();
      }
    });
    var sidebarAnyclickClose = $sidebar.data('sidebarAnyclickClose'); // Allows to close

    if (typeof sidebarAnyclickClose !== 'undefined') {
      $('.wrapper').on('click.sidebar', function (e) {
        // don't check if sidebar not visible
        if (!$body.hasClass('aside-toggled')) return;
        var $target = $(e.target);

        if (!$target.parents('.aside-container').length && // if not child of sidebar
        !$target.is('#user-block-toggle') && // user block toggle anchor
        !$target.parent().is('#user-block-toggle') // user block toggle icon
        ) {
            $body.removeClass('aside-toggled');
          }
      });
    }
  }

  function sidebarAddBackdrop() {
    var $backdrop = $('<div/>', {
      'class': 'sidebar-backdrop'
    });
    $backdrop.insertAfter('.aside-container').on("click mouseenter", function () {
      removeFloatingNav();
    });
  } // Open the collapse sidebar submenu items when on touch devices
  // - desktop only opens on hover


  function toggleTouchItem($element) {
    $element.siblings('li').removeClass('open');
    $element.toggleClass('open');
  } // Handles hover to open items under collapsed menu
  // -----------------------------------


  function toggleMenuItem($listItem) {
    removeFloatingNav();
    var ul = $listItem.children('ul');
    if (!ul.length) return $();

    if ($listItem.hasClass('open')) {
      toggleTouchItem($listItem);
      return $();
    }

    var $aside = $('.aside-container');
    var $asideInner = $('.aside-inner'); // for top offset calculation
    // float aside uses extra padding on aside

    var mar = parseInt($asideInner.css('padding-top'), 0) + parseInt($aside.css('padding-top'), 0);
    var subNav = ul.clone().appendTo($aside);
    toggleTouchItem($listItem);
    var itemTop = $listItem.position().top + mar - $sidebar.scrollTop();
    var vwHeight = document.body.clientHeight;
    subNav.addClass('nav-floating').css({
      position: isFixed() ? 'fixed' : 'absolute',
      top: itemTop,
      bottom: subNav.outerHeight(true) + itemTop > vwHeight ? 0 : 'auto'
    });
    subNav.on('mouseleave', function () {
      toggleTouchItem($listItem);
      subNav.remove();
    });
    return subNav;
  }

  function removeFloatingNav() {
    $('.sidebar-subnav.nav-floating').remove();
    $('.sidebar-backdrop').remove();
    $('.sidebar li.open').removeClass('open');
  }

  function isTouch() {
    return $html.hasClass('touch');
  }

  function isSidebarCollapsed() {
    return $body.hasClass('aside-collapsed') || $body.hasClass('aside-collapsed-text');
  }

  function isSidebarToggled() {
    return $body.hasClass('aside-toggled');
  }

  function isMobile() {
    return document.body.clientWidth < APP_MEDIAQUERY.tablet;
  }

  function isFixed() {
    return $body.hasClass('layout-fixed');
  }

  function useAsideHover() {
    return $body.hasClass('aside-hover');
  }
})(); // SLIMSCROLL
// -----------------------------------


(function () {
  'use strict';

  $(initSlimsSroll);

  function initSlimsSroll() {
    if (!$.fn || !$.fn.slimScroll) return;
    $('[data-scrollable]').each(function () {
      var element = $(this),
          defaultHeight = 250;
      element.slimScroll({
        height: element.data('height') || defaultHeight
      });
    });
  }
})(); // Table Check All
// -----------------------------------


(function () {
  'use strict';

  $(initTableCheckAll);

  function initTableCheckAll() {
    $('[data-check-all]').on('change', function () {
      var $this = $(this),
          index = $this.index() + 1,
          checkbox = $this.find('input[type="checkbox"]'),
          table = $this.parents('table'); // Make sure to affect only the correct checkbox column

      table.find('tbody > tr > td:nth-child(' + index + ') input[type="checkbox"]').prop('checked', checkbox[0].checked);
    });
  }
})(); // TOGGLE STATE
// -----------------------------------


(function () {
  'use strict';

  $(initToggleState);

  function initToggleState() {
    var $body = $('body');
    var toggle = new StateToggler();
    $('[data-toggle-state]').on('click', function (e) {
      // e.preventDefault();
      e.stopPropagation();
      var element = $(this),
          classname = element.data('toggleState'),
          target = element.data('target'),
          noPersist = element.attr('data-no-persist') !== undefined; // Specify a target selector to toggle classname
      // use body by default

      var $target = target ? $(target) : $body;

      if (classname) {
        if ($target.hasClass(classname)) {
          $target.removeClass(classname);
          if (!noPersist) toggle.removeState(classname);
        } else {
          $target.addClass(classname);
          if (!noPersist) toggle.addState(classname);
        }
      } // some elements may need this when toggled class change the content size


      if (typeof Event === 'function') {
        // modern browsers
        window.dispatchEvent(new Event('resize'));
      } else {
        // old browsers and IE
        var resizeEvent = window.document.createEvent('UIEvents');
        resizeEvent.initUIEvent('resize', true, false, window, 0);
        window.dispatchEvent(resizeEvent);
      }
    });
  } // Handle states to/from localstorage


  var StateToggler = function StateToggler() {
    var STORAGE_KEY_NAME = 'jq-toggleState';
    /** Add a state to the browser storage to be restored later */

    this.addState = function (classname) {
      var data = Storages.localStorage.get(STORAGE_KEY_NAME);
      if (data instanceof Array) data.push(classname);else data = [classname];
      Storages.localStorage.set(STORAGE_KEY_NAME, data);
    };
    /** Remove a state from the browser storage */


    this.removeState = function (classname) {
      var data = Storages.localStorage.get(STORAGE_KEY_NAME);

      if (data) {
        var index = data.indexOf(classname);
        if (index !== -1) data.splice(index, 1);
        Storages.localStorage.set(STORAGE_KEY_NAME, data);
      }
    };
    /** Load the state string and restore the classlist */


    this.restoreState = function ($elem) {
      var data = Storages.localStorage.get(STORAGE_KEY_NAME);
      if (data instanceof Array) $elem.addClass(data.join(' '));
    };
  };

  window.StateToggler = StateToggler;
})();
/**=========================================================
 * Module: trigger-resize.js
 * Triggers a window resize event from any element
 =========================================================*/


(function () {
  'use strict';

  $(initTriggerResize);

  function initTriggerResize() {
    var element = $('[data-trigger-resize]');
    var value = element.data('triggerResize');
    element.on('click', function () {
      setTimeout(function () {
        // all IE friendly dispatchEvent
        var evt = document.createEvent('UIEvents');
        evt.initUIEvent('resize', true, false, window, 0);
        window.dispatchEvent(evt); // modern dispatchEvent way
        // window.dispatchEvent(new Event('resize'));
      }, value || 300);
    });
  }
})(); // Custom Code
// -----------------------------------


(function () {
  'use strict';

  $(initCustom);

  function initCustom() {// custom code
  }
})();




