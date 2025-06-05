from jinja2 import Template

def generate_statement(compiled_template: Template, kwarg: dict) -> str:
    return compiled_template.render(**kwarg)

template_str = "{{ x }}時の{{ y }}は{{ z }}"
compiled_template = Template(template_str)

argument = {"x": 12, "y": "気温", "z": 22.4}

print(generate_statement(compiled_template, argument))
