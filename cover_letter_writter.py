#!/usr/bin/env python3
# This is a script that takes the name of a company and a job title, and adds that to a boiler plate cover letter .

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

job_title = input("What is the job title?\n")
company_name = input("What is the job organisation name?\n")

styles = getSampleStyleSheet()
styles['Normal'].fontName = 'Times-Roman'  # Set the font name to Liberation Serif
w, h = A4

doc = SimpleDocTemplate("/home/kubuntu-user/Temporary_Workspace/cover_letter_baljit_sanghera.pdf", pagesize=A4)

doc.title = "Cover Letter"
doc.author = "Baljit Sanghera"
doc.subject = f"Cover Letter for {job_title} at {company_name}"

story = []

text = f"""
I am writing to express my strong interest in the {job_title} position at {company_name}. As an experienced
cyber security enthusiast, I am excited about the opportunity to contribute my skills and expertise to
{company_name}’s esteemed team.<br /><br />
I have reviewed the job posting and believe that my background aligns well with the requirements of
the role. I’ve obtained the CompTIA Network+, Security+ and LPI Linux Essentials. Through
obtaining my certifications I’ve built a solid foundation in security, networking, Linux, and
coding/scripting, I am well-equipped to assess and mitigate cyber security risks associated with third-
party vendors.<br /><br />
In my experience as an Ecommerce Fraud Analyst I’ve developed rules based policies to differentiate
between threat actors and legitimate users. I’ve also carried out open source intelligence(OSINT) to
determine if flagged users will be allowed access to my organization’s services. As a fraud analyst I
maintain knowledge of current and past threats, tactics and procedures used by different types of threat
actors. I also have experience automating tasks with Bash, Python, VBA, and Java.<br /><br />
As a detail-oriented and analytical professional, I am able to assess, analyze, and mitigate security
risks using a proactive and strategic approach. I am a strong communicator and collaborator, able to
effectively work with cross-functional teams and communicate complex technical concepts to
stakeholders at all levels.<br /><br />
I am excited about the opportunity to join the team at {company_name} as a {job_title}, and I am confident that
my skills, experience, and passion for cyber security make me a valuable asset to your organization. I
am available at your convenience for an interview to discuss my qualifications in detail.<br /><br />
Thank you for considering my application.<br /><br />
Sincerely,<br /><br /><br />
Baljit Sanghera
"""

paragraph = Paragraph(text, styles["Normal"])
story.append(paragraph)

doc.build(story)
