import yaml
import importlib
import time

if __name__ == "__main__":
    try:
        with open("src/__site__.yaml", "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        print("Error: __site__.yaml not found.")
        exit(1)

    try:
        template = importlib.import_module(f"src.templates.{config['template']}.template")
    except ModuleNotFoundError:
        print(f"Error: template {config['template']} not found.")
        exit(1)

    copyright = config["copyright"] if "copyright" in config else None
    navbar = config["navbar"] if "navbar" in config else []
    icon = config["icon"] if "icon" in config else None

    base = template.Template(title=config["title"], copyright=copyright, navbar=navbar, icon=icon)

    old = {}
    while True:
        for page in config["pages"]:
            try:
                with open(f"src/{page}.yaml", "r") as f:
                    page_config = yaml.load(f, Loader=yaml.FullLoader)
                if page not in old or old[page] != page_config:
                    print(f"Rendering {page}")
                    old[page] = page_config
                    content = ""
                    if "sections" in page_config:
                        for section in page_config["sections"]:
                            section_template = template.sections[section["type"]]
                            content += section_template.render(section)
                    with open(f"{page}.html", "w") as f:
                        code = base.render(content, page_config, active=page)
                        f.write(code)
            except Exception as e:
                print(f"Error: {e}")
                old[page] = None
        time.sleep(1)

    

    