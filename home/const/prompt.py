basic_53_prompt = '''
Please grade the Korean paragraph below IN ENGLISH:
1. Content and Task Completion (7 points)
Excellent (6-7 points), Average (3-5 points), Poor (0-2 points).
- Did the student complete the assigned task thoroughly?
- Is the content relevant to the topic?
- Did the student use a variety of expressions?
2. Structure (7 points)
Excellent (6-7 points), Average (3-5 points), Poor (0-2 points).
- Is the writing clear and logical?
- Are the paragraphs well-organized?
- Did the student use transition words effectively?
3. Language Usage (16 points)
Excellent (14-16 points), Average (8-12 points), Poor (0-6 points)
- Did the student use a variety of grammar and vocabulary?
- Is the grammar, vocabulary, and spelling accurate?
- Is the writing style appropriate for the purpose)?

* For each area, please:
- Point out any issues you find, especially grammatical errors.
- Explain why it's an issue and how it could be improved, return the fixed sentence in Korean.
- (Optional) Suggest revisions for better clarity and naturalness.

Paragraph:

'''

basic_54_prompt = '''
Please grade the Korean paragraph below based on the grading rubrics below IN ENGLISH:

1. Content and Task Completion (12 points)
Excellent (9-12 points), Average (5-8 points), Poor (0-4 points).
- Did the student complete the task according to the instructions?
- Is the content relevant to the topic?	
- Did the student express the content in a rich and varied way?	
2. Structure Development (12 points)
Excellent (9-12 points), Average (5-8 points), Poor (0-4 points).
- Does the essay have a clear and logical structure?
- Is the central idea clearly presented?
- Are the transitions between ideas clear and cohesive?
3. Language Use (26 points)
Excellent (20-26 points), Average (12-18 points), Poor (0-10 points).
- Does the student use a varied and rich vocabulary?
- Is the grammar and spelling accurate?
- Is the writing style appropriate for the assignment?

* For each area, please:
- Point out any issues you find, especially grammatical errors.
- Explain why it's an issue and how it could be improved, return the fixed sentence in Korean.
- (Optional) Suggest revisions for better clarity and naturalness.

Topic:
$topic
Paragraph: 

'''
