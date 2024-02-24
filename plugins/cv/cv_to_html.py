from jinja2 import Environment, PackageLoader
import os


def generate_html(page_data, config_data, cv_data):
    # Set template
    env = Environment(loader=PackageLoader('main', 'templates'))
    cv_template = env.get_template('page_cv_web.html')

    # Set file path
    file_path = 'build/cv.html'

    # Render temp html
    page_html = cv_template.render(data=page_data, config_data=config_data, cv_data=cv_data)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as output_page_file:
        output_page_file.write(page_html)
