import yaml

class Properties:
    email_properties = {}
    template = ""

    def __init__(self):
        yaml_props = yaml.load(open('properties.yaml', 'r'))

        self.email_properties["fromAddress"] = yaml_props["email"]["send"]["from"]
        self.email_properties["replyToAddress"] = yaml_props["email"]["send"]["replyto"]
        self.email_properties["subject"] = yaml_props["email"]["send"]["subject"]

        self.template = yaml_props["email"]["template"]