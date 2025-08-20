



1:
Important instruction: ID card validation is a must!
*
Ask candidates to show a Government issued ID card at the very beginning of the interview.  If the candidate is not ready to show the ID, then terminate the interview and mark candidate as a “Reject”.


2:

Information only: Introductory script and guidelines
Introduction script for interview kick off

Hello [Candidate name], am I pronouncing your name correctly? 
Thank you for taking the time to speak with me today. My name is [Your Name] and I’ll be conducting your interview for the [Job name] role. I’m excited to learn more about your technical skills and experiences.
Before we begin the technical assessment, I would love a brief introduction from yourself to learn a bit about your background and work experience.
Great, so as you may know, Turing is a platform that connects world-class developers like yourself to top U.S. and Silicon Valley companies. We’re not just looking to fill a slot, we are focused on finding consistent long-term work that aligns with your career goals and offers you the opportunity to work on challenging projects that drive growth and innovation.
As part of that mission, we have a vetting process designed to match you with roles that are a good fit for your experiences and to help you become an integral part of the development team you join.
Now, let's get into the technical assessment. This is a crucial part of our process. We want to see how you approach problems, your coding proficiency, and your overall compatibility with the work environment our clients offer.
During this process, please feel free to ask questions and communicate your thought process. We are not just evaluating your final answers but also your approach to problem-solving – this is key to understanding how you'll integrate with teams and projects.







3:
Information: If candidate begins to ask questions about vetting process + client + other information

If candidate begins to ask questions about vetting process + client + other information

At a high level, the way Turing’s process is set up is to first evaluate your qualifications and ability to succeed in the clients role, second to prepare your profile and share it with the client, third if the client is interested in meeting you, we will help to schedule an interview between you and the client, finally depending on the outcome of that interview you’ll be onboarded for a two week trial period with the client before finally transitioning into the full engagement.
That said – this call is focused on evaluating your technical capabilities and I am not from the hiring team.  I would suggest you reserved your questions for the HR person working with you - so that you get an accurate information.



4:
Selection Criteria : (IMPORTANT)
Please mark the skills rating out of 10.
 

Candidates with the overall rating of 7,8,9,10 can be considered SELECT

 

Candidates with overall rating of 6,5,4,3,2,1 should be REJECT.


5:

Candidate's screen sharing is mandatory (please follow the instructions)
Please ask the candidate to share their entire screen. When a candidate shares their entire screen, you will typically be able to see the candidate's taskbar (or dock on macOS) at the bottom of the screen.


6:

Prior project knowledge
*
Check the prior project knowledge. Ask questions about projects mentioned in CV/ resume of candidate. Tweak the project & ask about alternate problem around similar line.









7:
IMPORTANT NOTES FOR CANDIDATE: 

Provide your answer in the coding window.  Title , etc. – do not delete the content from when you go to to the next iteration.  Retain all your content. 
Share your ENTIRE screen while attempting this question. 
 

Iteration 1 

 

User: How can I use Python to automate tasks? 

 

Assistant: Python is great for automation. For instance, you can automate file handling tasks like renaming multiple files in a directory: 

import os 

 

def rename_files(directory, prefix): 
    for count, filename in enumerate(os.listdir(directory)): 
        dst = f"{prefix}_{str(count)}.jpg" 
        src = f"{directory}/{filename}" 
        dst = f"{directory}/{dst}" 
        os.rename(src, dst) 
 
# Example usage: 
rename_files("/path/to/directory", "image") 
Iteration 2 

 

User: < Complete 1 > 

 

Assistant: You can use the schedule library to run scripts at specific intervals: 

import schedule 

import time 

 

def job(): 
    print("Executing scheduled task...") 
 
# Schedule job every 10 minutes 
schedule.every(10).minutes.do(job) 
 
while True: 
    schedule.run_pending() 
    time.sleep(1) 
 

Iteration 3 

 

User: Can I automate web scraping tasks with Python? 

 

Assistant: < Complete 2 > 

 

Iteration 4 

 

User: < Complete 3 > 

 

Assistant: < Complete 4 >






8:

Problem Statement
You are tasked with analyzing health insurance claims data represented in a JSON format. The data includes information about patients and their associated claims. You need to perform several tasks to extract insights and analyze patterns in the claims data.

 

JSON: 

{
"patients": [
    {
        "id": "P001",
        "claims": [
            {
                "id": "C001",
                "amount": 100,
                "billingCode": "B001",
                "date": "2024-01-01"
            },
            {
                "id": "C002",
                "amount": 200,
                "billingCode": "B001",
                "date": "2024-01-05"
            },
            {
                "id": "C003",
                "amount": 150,
                "billingCode": "B002",
                "date": "2024-01-10"
            }
        ]
    }
]
}
 

Tasks
Task 1: Extract Related Claims
Part A: Write a function to extract all claims related to a given claim ID from the provided JSON data. Return a list of related claim IDs.
Part B: Using the same JSON data, write a function to find the maximum claim amount in the last 'n' days for a given patient ID.
Task 2: Merge Claim Data
Part A: Write a function to merge claims for a specific patient and billing code. Return the merged claim data as a JSON object.
Part B: Using the same JSON data, write a function to find the most frequently occurring billing code for a given patient ID.
Task 3: Filter Claims by Date Range
Part A: Write a function to filter claims for a given patient within a specific date range. Return the filtered claims as a list.
Part B: Using the same JSON data, write a function to find the length of the longest contiguous subarray of claims with the same billing code for a given patient ID.
Task 4: Group Claims
Part A: Write a function to group claims by patient age and treatment type. Return a nested JSON object showing the grouped claims.
Part B: Using the same JSON data, write a function to determine if there exists a valid sequence of billing codes where each subsequent billing code is greater than the previous one, and return the sequence.
Task 5: Analyze Fraud Patterns
Part A: Write a function to analyze patterns of potential fraud in the claims data. Return a list of suspicious claims based on defined criteria (e.g., repeated claims for the same billing code).
Part B: Using the same JSON data, write a function to find the first unique billing code for a specific patient.
Instructions for Candidates
Implement the required functions as described in each task.
Ensure your implementation is efficient and readable.








Issues:
2A: What to merge? This seems more of a "data filtering" question than a merging one.

Task 4: Group Claims
Part A: Write a function to group claims by patient age and treatment type. Return a nested JSON object showing the grouped claims.

THERE IS NO TREATMENT TYPE VALUE IN INPUT JSON.



9:

Information: Outro
Closing and next steps

"The interview is now over. We'd like to take a few minutes to discuss what a typical day might entail for you in this role. Our aim is to ensure you have a clear understanding of the role and responsibilities, with no surprises on your first day.This position is within a project with one of the foundational LLM companies. The goal is to assist these foundational LLM companies in enhancing their Large Language Models.One way we help these companies improve their models is by providing them with high-quality proprietary data. This data serves two main purposes: first, as a basis for fine-tuning their models, and second, as an evaluation set to benchmark the performance of their models or competitor models. The project's goal is to create this high-quality dataset, and you will have a critical role to play.
We have two approaches to generate this proprietary data: Supervised Fine Tuning (SFT) and Reinforcement Learning from Human Feedback (RLHF). RLHF typically involves interacting with the LLM model, providing feedback on its output, and offering rewrites when necessary. In SFT, we generate numerous golden prompt-response pairs, devoid of model interaction.For example, in SFT, you might take an open-source dataset, ask data analysis questions, and write corresponding Python code to solve them. A collection of 5k-10k such samples could form the dataset for model fine-tuning.In RLHF, you might upload a dataset to a tool provided by the customer, ask data analysis questions, and evaluate the outputs generated by two versions of the LLM model. You'd compare these outputs and provide feedback, which is then used to fine-tune the models."

 

 

Here's what you can expect moving forward:

If you are selected to proceed to the next stage, you will be introduced to the specific client who is interested in hiring you. They have their own interview process tailored to their needs.
Please be prepared to engage in another technical interview from the client that may delve deeper into your core skill areas. They might also wish to discuss your experience in a conversational format to understand how you could contribute to their team.
Along with the technical evaluation, clients will be interested in your communication skills, cultural fit, and your approach to collaboration and problem-solving within a team. So, it’s important to showcase your interpersonal skills as much as your technical abilities.
I highly recommend that you review the job description once more to refresh your understanding of the role you are being considered for. Also, it would be advantageous for you to revisit some of the questions I asked during our interview or similar ones. Practice articulating your thoughts and processes clearly, as this could be a significant factor during your conversation with the client.
Our talent operations specialist will reach out to you with updates on next steps if you are selected.They will be your point of contact and are there to help guide you through the next stages of the process.
Thank you again for your collaboration, [candidate name] 


