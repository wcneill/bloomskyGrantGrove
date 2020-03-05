import bloomsky_api as bs
import os
from jinja2 import Environment, FileSystemLoader


def get_photo_url():
    """
    pulls down python dictionary in JSON format from BloomSky's server and parses the image URL from it.
    :return: the url containing the latest bloomsky image from our Grant Grove location.
    """
    client = bs.BloomSkyAPIClient(api_key='pr-wrNbhiNjPoc6wtLS96NbVzeCTrNal')
    data = client.get_data()[0] # Dictionary formatted like JSON, if you want data besides the latest image
    return data.get('outdoor').get('image_url')

def generate_html(template_file_name, final_file_name):
    """
    uses an HTML template to generate page dynamically that will contain the updated photo on request

    :param template_file_name: The name of the html template
    :param final_file_name: The name of the final html file you wish your server to respond with
    :return:
    """
    root = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(root, 'templates')
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file_name)
    final_path = os.path.join(root, 'html', final_file_name)

    with open(final_path, 'w') as fh:
        fh.write(template.render(photo_url=get_photo_url()))


if __name__ == '__main__':
    generate_html('template.html', 'final.html')
    # The file names above can be whatever you want. Just make sure they match what's in your directory.