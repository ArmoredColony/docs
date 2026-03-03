# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Extensions'
copyright = '2026, Armored Colony'
author = 'Armored Colony'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#6b7cff",
        "color-brand-content": "#7a8bff",
        "color-link": "#ff7a5c",
        "color-background-primary": "#0f172a",
        "color-background-secondary": "#1a2238",
    },
    "dark_css_variables": {
        "color-brand-primary": "#6b7cff",
        "color-brand-content": "#7a8bff",
        "color-link": "#ff7a5c",
        "color-background-primary": "#0f172a",
        "color-background-secondary": "#1a2238",
    },
}