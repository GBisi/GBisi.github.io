class Template:
    def __init__(self, title, copyright=None, navbar=[], icon=None):
        self.title = title
        self.copyright = copyright
        self.navbar = navbar
        self.icon = icon
        self.mail_bookmark = '%%MAIL%%'
        self.mail = '`T\\\_gb-Z\\\hfXccX!U\\\\f\\\VV[\\\T3c[W!ha\\\c\\\!\\\g'

    def render(self, content, page_config, active=None):
        if "type" in page_config and page_config["type"] == "lp":
            return self.render_lp(page_config)
        else:
            return self.render_page(content, page_config, active)
        
    def render_lp(self, page_config):
        html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{self.title}</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <link rel="stylesheet" href="src/templates/academic_resume_js/academic-resume.css">
        <link rel=stylesheet href=https://cdnjs.cloudflare.com/ajax/libs/academicons/1.9.0/css/academicons.min.css integrity="sha512-W4yqoT1+8NLkinBLBZko+dFB2ZbHsYLDdr50VElllRcNt2Q4/GSs6u71UHKxB7S6JEMCp5Ve4xjh3eGQl/HRvg==" crossorigin=anonymous>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">  
        <meta name="viewport" content="width=device-width, initial-scale=1">
    """
        if self.icon is not None:
            html += f"""<link href="{self.icon}" rel="shortcut icon" type="image/vnd.microsoft.icon" />"""
        html+="""
        <script src="src/templates/academic_resume_js/obfuscation.js" defer></script>
            <script>
            document.addEventListener("DOMContentLoaded", function(){
            var els = document.getElementsByTagName("a");
            for (var i = 0, l = els.length; i < l; i++) {
                var el = els[i];
                if (el.href.includes("%%MAIL_BOOKMARK%%")) {
                    el.href = decode("%%MAIL_DECODED%%");
                }
            }});
            </script>
        </head>
    <body class="lp">
        """.replace("%%MAIL_DECODED%%", self.mail).replace("%%MAIL_BOOKMARK%%", self.mail_bookmark)

        html += f"""
        <!-- Landing page -->
        <div class="container">
            <div class="row lp-row">
                <div class="col">
                    <img class="lp-pic" alt="{page_config["alt_img"]}" src="{page_config["img"]}">
                    <h1 class="lp-title">{page_config["title"]}</h1>
                    <h2 class="lp-subtitle">{page_config["sub"]}</h2>
                    <h2 class="lp-subtitle">{page_config["desc"]}</h2>
                </div>
            </div>
                """

        if len(self.navbar) > 0:
            html += f"""
            <div class="row lp-row">
                <div class="col">
                """
            for item in self.navbar:
                name = list(item.keys())[0]
                if name != "_home_":
                    href = item[name]
                    html += f"""<a class="btn lp-btn" href="{href}">{name}</a>"""

        html += f"""
            </div>   
    </div>"""

        if "socials" in page_config:
            html += f"""<div class="row lp-row">
         <div class="col">"""
            
            for item in page_config["socials"]:
                html += f"""
                <a href="{item["link"]}">  <i class="{item["icon"]}" style="font-size:45px;color:#cccccc;"></i> </a> &thinsp;
                """

        html+=f"""   
            </div>
            </div>
            <div class="row lp-row">
                <div class="col">
                    <img class="lp-logo" alt="{page_config["alt_logo"]}" src="{page_config["logo"]}">
                </div>
            </div>
        </div>"""


        if self.copyright is not None:
                html += f"""
                <!-- Copyright footer -->
            <footer class="footer pt-4">
                <div class="container" style="text-align: center;">
                <span class="text-muted" style="color: #ccc!important">{self.copyright}</span>
                </div>
            </footer>"""

        html += """
            <!-- Scripts -->
            <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
        </body>
    </html>"""

        return html

    def render_page(self, content, page_config, active=None):
        html = f"""<!DOCTYPE html>
<html lang="en">
    <head>
        <title>{self.title}</title>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <link rel="stylesheet" href="src/templates/academic_resume_js/academic-resume.css">
        <link rel=stylesheet href=https://cdnjs.cloudflare.com/ajax/libs/academicons/1.9.0/css/academicons.min.css integrity="sha512-W4yqoT1+8NLkinBLBZko+dFB2ZbHsYLDdr50VElllRcNt2Q4/GSs6u71UHKxB7S6JEMCp5Ve4xjh3eGQl/HRvg==" crossorigin=anonymous>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">  
        <meta name="viewport" content="width=device-width, initial-scale=1">
    """
        if self.icon is not None:
            html += f"""<link href="{self.icon}" rel="shortcut icon" type="image/vnd.microsoft.icon" />"""
        html+="""
            <script src="src/templates/academic_resume_js/obfuscation.js" defer></script>
            <script>
            document.addEventListener("DOMContentLoaded", function(){
            var els = document.getElementsByTagName("a");
            for (var i = 0, l = els.length; i < l; i++) {
                var el = els[i];
                if (el.href.includes("%%MAIL_BOOKMARK%%")) {
                    el.href = decode("%%MAIL_DECODED%%");
                }
            }});
            </script>
        </head>
    <body>
        """.replace("%%MAIL_DECODED%%", self.mail).replace("%%MAIL_BOOKMARK%%", self.mail_bookmark)

        if len(self.navbar) > 0:
            home = "Home"
            for item in self.navbar:
                if "_home_" in item:
                    home = item["_home_"]
            html += f"""
            <!-- Navigation Bar-->
            <nav class="navbar fixed-top navbar-expand-lg navbar-dark cp-navbar">
                <a class="navbar-brand cp-brand" href="index.html">{home}</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#jsNavBar" aria-controls="jsNavBar" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="jsNavBar">
                    <div class="navbar-nav ml-auto">
                """
            for item in self.navbar:
                name = list(item.keys())[0]
                if name != "_home_":
                    href = item[name]
                    if active is not None and href.startswith(active):
                        html += f"""
                        <a class="nav-item nav-link active" href="{href}">{name}</a>"""
                    else:
                        html += f"""
                            <a class="nav-item nav-link" href="{href}">{name}</a>"""
            html+= """
                    </div> 
                </div>
            </nav>
            """

        html += content

        if self.copyright is not None:
            html += f"""
            <!-- Copyright footer -->
        <footer class="footer pt-4">
            <div class="container" style="text-align: center;">
              <span class="text-muted">{self.copyright}</span>
            </div>
        </footer>"""

        html += """
        <!-- Scripts -->
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q4orYjBQndcko6MimVbzY0tgp4pWB4lZ7lr30WKz0vr/aWKhXdBNmNb5D92v7s" crossorigin="anonymous"></script>
    </body>
</html>"""

        return html


class SectionTextImgRight:
    def render(config):
        html = """<div class="container">"""
        if "title" in config:
            html += f"""
            <div class="row pt-4">
                <div class="col">
                    <h4 class="cp-title">{config["title"]}</h4>
                </div>
            </div>"""
        return html+f"""
        <div class="row pt-4">
                <div class="col-xl-8 col-lg-8 col-md-8">
                    <p>
                        {config["text"]}
                    </p>
                </div>
                <div class="col-xl-4 col-lg-4 col-md-4" style="text-align: center;">
                    <img class="cp-pic pt-1" src="{config["img"]}" alt="{config["img_alt"]}">
                </div>
            </div>
        </div>
        """

class SectionTimeline:
    def render(config):
        html = """<div class="container">"""
        if "title" in config:
            html += f"""
            <div class="row pt-4">
                <div class="col">
                    <h4 class="cp-title">{config["title"]}</h4>
                </div>
            </div>"""
        html += """
        <div class="row">
                <div class="row">
                    <div class="col">
                        <ul class="timeline">
        """
        for item in config["items"]:
            html += f"""<li>{item}</li>"""
        html += """
        </ul>
                    </div>
                </div>
            </div>
        </div>"""
        return html

class SectionText:
    def render(config):
        if "title" in config:
            return f"""
            <div class="container">
            <div class="row pt-4">
                <div class="col">
                    <h4 class="cp-title">{config["title"]}</h4>
                    {config["text"]}
                </div>   
            </div>
            </div>
        """
        return f"""<div class="container">
        <div class="row pt-4">
                <div class="col">
                    {config["text"]}
                </div>   
            </div>
        </div>
        """

class SectionBox:
    def render(config):
        html = """<div class="container">"""
        if "title" in config:
            html += f"""
            <div class="row pt-4">
                <div class="col">
                    <h4 class="cp-title">{config["title"]}</h4>
                </div>
            </div>
            <div class="row">"""
        else:
            html += """
            <div class="row pt-4">
            """
        html += f"""
                <div class="col">
                    <ul class="list-group">
                        <li class="list-group-item cp-shaded"><span class="cp-title">{config["main"]}</span></li>
        """
        for item in config["items"]:
            html += f"""<li class="list-group-item">{item}</li>
            """
        html += f"""
                    </ul>
                </div>
            </div>
        """
        return html+f"""</div>"""


class SectionBigBox:
    def render(config):
        html = """<div class="container">"""
        if "title" in config:
            html += f"""
            <div class="row pt-4">
                <div class="col">
                    <h4 class="cp-title">{config["title"]}</h4>
                </div>
            </div>
            <div class="row">"""
        else:
            html += """
            <div class="row pt-4">
            """
        html += f"""
        
                <div class="col">                    
                    <div class="jumbotron cp-shaded">
                        <h3 class="cp-title">{config["main"]}</h3>
                        <h5>
                            {config["sub"]}
                        </h5>
                        <hr class="my-4">
                        <p>
                            {config["text"]}
                        </p>
                    </div>
                </div>
            </div>
            </div>"""
        return html

class SectionContacts:
    def render(config):
        html = """<div class="container">"""
        if "title" in config:
            html += f"""
            <div class="row pt-4">
                <div class="col">
                    <h4 class="cp-title">{config["title"]}</h4>
                </div>
            </div>
            <div class="row">"""
        else:
            html += """
            <div class="row pt-4">
            """
        html += f"""
                <div class="col">                    
                    <div class="jumbotron cp-shaded">
                    """

        if "upper_text" in config:
            html += f"""
                        <div class="row cp-contact-info">
                            <div class="col">
                                {config["upper_text"]}
                            </div>
                        </div>
                        """

        html += f"""
                        <table class="table table-borderless">
                            <tbody>
                            """

        for item in config["items"]:
            html += f"""
                                <tr class="cp-contact-info">
                                    <td class="pr-1" style="text-align: center; vertical-align: middle;">
                                        <i class='{item["icon"]}' style='font-size:50px'></i>
                                    </td>
                                    <td class="pl-1" style="vertical-align: middle;">
                                        {item["text"]}
                                    </td>
                                </tr>
                                """

        html += f"""
                            </tbody>
                        </table>
                        """

        if "lower_text" in config:
            html += f"""
                        <div class="row cp-contact-info">
                            <div class="col">
                                {config["lower_text"]}
                            </div>
                        </div>
                        """


        html += f"""</div>
                </div>
            </div>
        </div>
        </div>"""

        return html

class SectionHr:
    def render(config):
        return """<div class="container"><hr class="my-4"></div>"""
    
class SectionHeader:

    def render(config):
        html = f"""<div class="lp">
    <div class="container">
    <div class="row lp-row">
        <div class="col">
        """
        if "img" in config:
            html += f"""
            <img class="lp-pic alt="{config["alt_img"]}" src="{config["img"]}">
            """
        
        html+=f"""
            <h1 class="lp-title">{config["title"]}</h1>
            <h2 class="lp-subtitle">{config["sub"]}</h2>
            <h2 class="lp-subtitle">{config["desc"]}</h2>
        </div>"""

        if "socials" in config:
            html += f"""<div class="row lp-row">
         <div class="col">"""
            
            for item in config["socials"]:
                html += f"""
                <a href="{item["link"]}">  <i class="{item["icon"]}" style="font-size:45px;color:#cccccc;"></i> </a>  &thinsp;
                """
            
            html += f"""
            </div>   
    </div>"""

        html += f"""
    </div>
<div class="row lp-row">
                    <div class="col">
                        <img class="lp-logo" alt="{config["alt_logo"]}" src="{config["logo"]}">
                    </div>
                </div>
                <div class="row lp-row">
                    <div class="col">
                    </div>
                    </div>
                </div>
            </div>
        """
        return html

sections = {
    "text_with_img_right": SectionTextImgRight,
    "timeline": SectionTimeline,
    "text": SectionText,
    "box": SectionBox,
    "big_box": SectionBigBox,
    "contacts": SectionContacts,
    "hr": SectionHr,
    "header": SectionHeader,
}