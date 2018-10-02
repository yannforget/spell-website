[![Build Status](https://travis-ci.org/yannforget/spell-website.svg?branch=master)](https://travis-ci.org/yannforget/spell-website)

# SpELL Website

## Description

The website is built using the static site generator [Hugo](https://gohugo.io/). Hugo documentation can be found [here](https://gohugo.io/documentation/).

Content files have to be provided in markdown ([cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet), [docs](https://daringfireball.net/projects/markdown/)).

## How-Tos...

### ...add a news

* Create a new `.md` file in the `content/news` directory.
* Add the relevant YAML metadata header and write your content in markdown.
* Commit your changes.

The content of the news will be automatically splitted when displayed on the homepage. You can manually add the `<!--more-->` divider where you want to split the article.

### ...add people

* Create a new `.md` file in the `content/person` directory.
* Add the relevant YAML metadata header: name, contact details, position, portrait...
* Optionally, add the content that will be displayed in the personal page.
* Commit your changes.

Personal publications will be automatically fetched from the provided bibliography (see below). The dimensions of the portraits must be `200x200px`.

### ...add a project

* Create a new `.md` file in the `content/project` directory.
* Add the relevant YAML metadata header and, optionally, a description of the project in markdown.

Related publications will be automatically fetched from the global bibliography files, provided that they are tagged accordingly in Zotero (i.e. the Zotero tag must be equal to the `ref` variable in the YAML header of the content file).

### ...add an image or a media

* Upload your file to the `static/images` directory.
* Commit your changes.

The image can now be used in all the content files. For example, if you added an image called `campusmap.png`, you can link to it in markdown:

``` markdown
![Map of the campus]("/images/campusmap.png")
```

### ...add a standalone page

* Create a new `.md` file in the `content/page` directory.
* Add the relevant YAML metadata header (only `title` is required), and the content of the page in markdown.

If you created the `teaching.md` page, it will be available at the following URL: `spell.ulb.be/page/teaching`.

### ...update the references

References are automatically fetched from the `.csv` files located in the `zotero/` directory. This files can be directly exported from Zotero by right-clicking on a collection in Zotero and selecting the `Export collection...` option (choose CSV as the export format). 

Files that contains the word `"external"` will be processed differently: the references contained in this file will not be displayed on the main publications page. However, they will be fetched to populate the bibliography of each person.

### ...update the homepage description

This description text is located in the `config.yaml` file. To change it, just edit the `description` variable. Likewise, you can change the `title` and the `brand` variables.

### ...add an entry to the menu

Entries displayed in the menu are defined in the `config.yaml` file (see the [hugo docs](https://gohugo.io/content-management/menus/) for details). For example, to add a `data` entry to the menu:

``` yaml
- Name: "Data"
  Weight: 8
  Identifier: "data"
  parent: "ressources"
  URL: "/page/data"
```

* `Name` : Name of the menu entry that is displayed.
* `Weight` : Weight of the entry that controls the display order.
* `Identifier` : Identifier of the menu entry that can be used for reference (see below).
* `parent` : Identifier of the parent menu entry. Here, the data menu entry is displayed under the ressources tab.
* `URL` : URL of the menu entry.
