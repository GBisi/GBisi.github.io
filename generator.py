import yaml
import csv


def generate_button(name, link):
    return '<a class="btn btn-box btn-box-link" href="' + link + '">' + name + '</a>'

def generate_abstract_button(name, abstract, id):
    #make a div hidden with abstract and then make a link and onclick show the div with collapse
    return '<a class="btn btn-box btn-box-link" data-toggle="collapse" href="#talk-'+str(id)+'" role="button" aria-expanded="false" aria-controls="talk-'+str(id)+'">' + name + '</a>'

def generate_publications(file):
    theses = {"type": "box", "main": "Theses", "items": []}
    publications = {"type": "box", "main": "Publications", "items": []}
    accepted = {"type": "box", "main": "Accepted for Publication", "items": []}

    with open(file, "r") as f:
        reader = csv.DictReader(open(file, "r"))
        id = 0
        for row in reader:
            s = ""

            if row["Type"] == "Journal":
                s += '<span class="badge badge-journal">&nbsp;&nbsp;</span> '
            elif row["Type"] == "Proceeding":
                s += '<span class="badge badge-proceedings">&nbsp;&nbsp;</span> '
            elif row["Type"] == "Volume":
                s += '<span class="badge badge-volume">&nbsp;&nbsp;</span> '
            else:
                s += '<span class="badge badge-misc">&nbsp;&nbsp;</span>  '

            s += row["Authors"] + ". "

            if row["DOI"] != "":
                s += '<span class="cp-publication-title"><a class="cp-link" href="'+ row["DOI"] + '">' + row["Title"] + '</a></span>. '
            else:
                s += '<span class="cp-publication-title">' + row["Title"] + '</span>. '

            s+= row["Venue"] + ", "

            if row["Year"] != "":
                s += row["Year"] + ". "

            buttons = ""

            # if row["BibTeX"] != "":
            #     buttons += generate_button("BibTeX", "assets/bibtex/"+row["BibTeX"])

            if row["Abstract"] != "":
                buttons += generate_abstract_button("Abstract", row["Abstract"], id)

            if row["DOI"] != "":
                buttons += generate_button("DOI", row["DOI"])
            
            if row["PDF"] != "":
                buttons += generate_button("PDF", "assets/publications/"+row["PDF"])

            if row["Repository"] != "":
                buttons += generate_button("Repository", row["Repository"])

            if row["Slides"] != "":
                buttons += generate_button("Slides", "assets/slides/"+row["Slides"])

            if row["Video"] != "":
                buttons += generate_button("Video", "assets/videos/"+row["Video"])

            if row["Poster"] != "":
                buttons += generate_button("Poster", "assets/posters/"+row["Poster"])

            if row["Citation"] != "":
                buttons += generate_button("Cite", "assets/citations/"+row["Citation"])

            if buttons != "":
                s += '<br>' + buttons

            if row["Abstract"] != "":
                s += '<div class="collapse" id="talk-'+str(id)+'">'+row["Abstract"]+'</div>'
                id += 1

            if row["Type"] == "Thesis":
                theses["items"].append(s)
            elif row["Published"] == "true":
                publications["items"].append(s)
            else:
                accepted["items"].append(s)

    accepted["items"].reverse()
    publications["items"].reverse()
    theses["items"].reverse()

    text = {
        "type": "text",
        "text":"""Please find below a comprehensive list of my publications. The colour boxes in front of each publication follow the <a class="cp-link" href="https://dblp.uni-trier.de/faq/What+is+the+meaning+of+the+colors+in+the+publication+lists.html">DBLP colour scheme</a>.
                        Indexed publications are also listed on
                        <a class="cp-link" href="https://www.csauthors.net/giuseppe-bisicchia/">csauthors.net</a>, 
                        <a class="cp-link" href="https://dblp.org/pid/296/0099.html">DBLP</a>, 
                        <a class="cp-link" href="https://scholar.google.com/citations?user=7PUTvtYAAAAJ&hl">Google Scholar</a>, 
                        <a class="cp-link" href="https://www.researchgate.net/profile/Giuseppe_Bisicchia">Research Gate</a>,  
                        <a class="cp-link" href="https://www.scopus.com/authid/detail.uri?authorId=57225906269">Scopus</a>,
                        <a class="cp-link" href="https://www.webofscience.com/wos/author/record/HNQ-1300-2023">WoS</a>, and
                        <a class="cp-link" href="https://orcid.org/0000-0002-1187-8391">ORCID</a>."""
    }

    full = {"sections": [text,accepted, publications, theses]}
    with open("src/publications.yaml", "w") as f:
        yaml.dump(full, f, default_flow_style=False)

if __name__ == "__main__":
    generate_publications("Publications.csv")