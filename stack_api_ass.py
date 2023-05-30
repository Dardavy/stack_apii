import requests
import pdfkit



num_questions = 50

def fetch_questions(endpoint, num_questions):
    response = requests.get(endpoint)
    data = response.json()
    questions = data["items"][:num_questions]
    return questions

def create_pdf(questions):
    html_content = "<html><head><style>img {max-width: 50%;}</style></head><body>"
    question_number = 1

    for question in questions:
        title = question["title"]
        views = question["view_count"]
        link = question["link"]

        # Check if the "imageURL" key exists in the dictionary
        if "imageURL" in question:
            image_url = question["imageURL"]
        else:
            image_url = ""  # Set a default value if the key is missing

        html_content += f"<h2>{question_number}. {title}</h2>"
        html_content += f"<p>Views: {views}</p>"
        html_content += f'<a href="{link}">{link}</a>'
        html_content += f'<img src="{image_url}"><br><br>'

        question_number += 1

    html_content += "</body></html>"
    

    
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_string(html_content, "questions.pdf", configuration=config)


def main():
    url = input("Enter the URL of the site: ")  # url exanple = api.stackexchange.com/2.3/questions?site=stackoverflow&pagesize=50&sort=votes
    endpoint = f"https://{url}"
    

    questions = fetch_questions(endpoint, num_questions)
    create_pdf(questions)
    print("PDF created successfully.")
    input ("Press enter to quit")

if __name__ == "__main__":
    main()