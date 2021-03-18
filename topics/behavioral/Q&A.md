## Q. Talk about an instance where you had to make a decision without enough information

A. In my recent project, we had given requirements to develop a product that is responsible for deploying the software on the Akamai platform to test out the new experiment. Although the end goal was clear, enough data on what measures we have to capture and analyze was not clear from the beginning. I proposed a multiple phase development plan that starts with capturing one or two metrics and extend the coverage as we develop more phases. This approach facilitate the development team to build a software that is clearly defined with requirements and expected outcomes.

## Q. Describe a situation when you did much more than it was expected from you to get the project done. Were your efforts recognized? By whom and how? How did that make you feel?

A. At my work, I was assigned to work on the project that migrate close to 200k policies from one database to another. The main task was to read policies from one database and dump into another with some minor transformations. This task was especially challenging due to the fact that policies in the database were keep getting added and updated. Although we had a check to make sure we don’t migrate same policy twice, I implemented a monitoring system that identifies the delta between two databases and reports anomalies to the team. It provided visibility into the migration process and immensely helped the team in fixing db inconsistencies. I was recognized by the lead about an extra effort I took to make migration process more robust.

## Q. Can you provide a situation where you think you made a significant impact on the product ?

## Q. Describe a time when you made a suggestion to improve something on the project that you were working on.

A. We had a legacy python application that used to dump log lines into local filesystem. Production environment used to report alerts of application slowdown and after careful investigation, I figured out that multiple threads used to write logs into one single file and when traffic increases, threads used to wait longer to get the write lock on the log file. It used to hold the incoming connection and client was experiencing timeouts in high traffic situations. I proposed a solution that delegate the logging work to another thread so that the main thread can hand over the log line to that thread and continue processing the request. This improved the performance of the server and saved thousands of dollars in cost to company. I was recognized with spot rewards.

## Q. Give me an example of the project or initiative that you started on your own. It can be a non-business one. What prompted you to get started?

A. In my team, we did not have a formal process on the code reviews and It was challenging in ensuring the quality of code review across the board. Due to cross geo teams, we also had a code review dependencies that sometime used to delay the code reviews and eventually used to affect the project timeline. I proposed a three step code review process that not only ensure the quality of the code reviews but also speeds up the code review process.

1. Team member will create an early feedback PR(pull request) right after the implementation is done. It gives the reviewers a chance to review the PR while person is working on the unit testing. It also reduces the chances of rewrite/redo the unit testing if feedbacks are related to design or structural side of the code.
2. Code reviewers would review the code based on the three major areas in the order. This will allows developer to utilize their time in areas that are business critical and rest can be either enforced by tools or process.
   1. P1 -> functional issues
   2. P2 -> code design flaws
   3. P3 -> cosmetic problems
3. Reviewer would set up a call if P1 and P2 reviews exceed the limit defined. This minimizes the time spend in going back and forth to come to a reasonable common ground. It also allows the reviewer to express their opinion behind the review comment in much more details.

## Q. Describe a situation in which you met a major obstacle in order to complete a project. How did you deal with it? What steps did you take?

A. In my previous project, I had to develop a
