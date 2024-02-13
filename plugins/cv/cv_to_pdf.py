from weasyprint import HTML, CSS
from jinja2 import Environment, PackageLoader
import os


def generate_pdf(page_data, config_data, cv_data, cv_private_data, public):
    # Set template
    env = Environment(loader=PackageLoader('main', 'templates'))
    cv_template = env.get_template('page_cv_print.html')

    # Set file path
    file_path = 'build/cv_temp.html'

    # Render temp html
    page_html = cv_template.render(data=page_data, config_data=config_data, cv_data=cv_data,
                                   cv_private_data=cv_private_data, public=public)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as output_page_file:
        output_page_file.write(page_html)

    # Generate pdf
    html = HTML(filename=file_path)
    css = CSS(filename='./assets/styles/cv.css')

    if public:
        os.makedirs('build/public', exist_ok=True)
        html.write_pdf('./build/public/cv-public.pdf', stylesheets=[css])

    else:
        os.makedirs('build/private', exist_ok=True)
        html.write_pdf('./build/private/cv-private.pdf', stylesheets=[css])

    # Remove temp html
    os.remove(file_path)
