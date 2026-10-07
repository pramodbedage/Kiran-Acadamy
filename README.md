# 🎓 Kiran Academy - Web & Software Development Learning Journey

Welcome to the **Kiran Academy** repository! This repository documents the practical assignments, hands-on tasks, and projects developed during training, covering **HTML5**, **Python**, and **Problem Solving / LeetCode**.

---

## 📑 Table of Contents
- [HTML Module Summary](#-html-module---everything-learned)
  - [1. HTML5 Document Structure](#1-html5-document-structure)
  - [2. Headings & Text Formatting](#2-headings--text-formatting)
  - [3. Working with Lists](#3-working-with-lists)
  - [4. Tables & Data Presentation](#4-tables--data-presentation)
  - [5. Forms & User Input Controls](#5-forms--user-input-controls)
  - [6. Media & Embedded Elements](#6-media--embedded-elements)
  - [7. Hyperlinks & Page Navigation](#7-hyperlinks--page-navigation)
- [📂 HTML Module Files & Projects](#-html-module-files--projects)
- [🐍 Other Modules Overview](#-other-modules-overview)
- [🚀 How to Run Locally](#-how-to-run-locally)

---

## 🌐 HTML Module - Everything Learned

In this module, we progressed from core HTML building blocks to building complete multi-section web portals with forms, multimedia, maps, and interactive elements.

### 1. HTML5 Document Structure
- **`<!DOCTYPE html>`**: Declares the document type and tells the browser to render using modern HTML5 standards.
- **`<html lang="en">`**: The root element of an HTML page with language specification.
- **`<head>`**: Container for metadata, character encoding, title, and viewport setup:
  - `<meta charset="UTF-8">`: Handles character encoding for global language support.
  - `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: Ensures responsive rendering across mobile and desktop.
  - `<title>`: Displays the page title in the browser tab.
- **`<body>`**: Encloses all visible content rendered on the webpage.

### 2. Headings & Text Formatting
- **Heading Tags (`<h1>` to `<h6>`)**: Define document hierarchy from main title (`<h1>`) down to sub-sections (`<h6>`).
- **Paragraphs (`<p>`)**: Separate blocks of text with automatic top and bottom margins.
- **Formatting Elements**:
  - `<b>` and `<strong>`: Bold text for visual emphasis or strong importance.
  - `<i>` and `<em>`: Italicized text for tone, definitions, or stress emphasis.
  - `<u>`: Underline text.
  - `<del>`: Strikethrough text representing deleted or retired information.
  - `<small>`: Smaller font size, ideal for captions, figures, and copyright notices.
  - `<center>`: Centers inline and block content horizontally.
  - `<hr>`: Thematic break / horizontal separator line between sections.
  - `<br>`: Line break without starting a new paragraph.
  - Character entities: `&copy;` (©), `&amp;` (&).

### 3. Working with Lists
- **Unordered Lists (`<ul>`)**: Bulleted lists with customizable bullet types (`type="disc"`, `type="circle"`, `type="square"`).
- **Ordered Lists (`<ol>`)**: Numbered lists with attributes:
  - `type="1|a|A|i|I"`: Specifies numbering style.
  - `start="n"`: Sets the starting number sequence.
  - `<li value="n">`: Overrides the counter for a specific list item.
- **Nested Lists**: Combining `<ul>` and `<ol>` to create multi-level course roadmaps and geographic hierarchies (States &rarr; Cities).

### 4. Tables & Data Presentation
Comprehensive table construction using semantic tags and styling attributes:
- **Core Elements**: `<table>`, `<caption>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `<th>`, `<td>`.
- **Merging Cells**:
  - `rowspan="n"`: Combines multiple rows into a single cell.
  - `colspan="n"`: Combines multiple columns across headers, summaries, or footers.
- **Table Attributes**:
  - `border`, `cellpadding`, `cellspacing`, `width`, `height`, `bgcolor`, `bordercolor`, `align`.
- **Advanced Table Features**:
  - `<colgroup>` and `<col span="n">`: Applies formatting across column groups.
  - Accessibility attributes: `scope="col|row"`, `headers`, `abbr`, `id`.
  - Nested tables: Embedding a `<table>` inside a `<td>` for detailed sub-records.

### 5. Forms & User Input Controls
Creating structured and validated user feedback and registration forms:
- **`<form action="..." method="...">`**: Encloses user input components.
- **`<fieldset>` and `<legend>`**: Groups related input controls with a decorative framed border and legend title.
- **`<label for="inputId">`**: Associates descriptive labels with input fields to improve user experience and accessibility.
- **`<input>` Types Learned**:
  - `type="text"`: Single-line text input (with `placeholder`, `size`, `name`, `required`).
  - `type="number"`: Numeric values with `min` and `max` constraints.
  - `type="email"`: Email input with automatic email format validation.
  - `type="tel"`: Telephone numbers.
  - `type="date"`: Built-in date picker calendar.
  - `type="time"`: Time selection input.
  - `type="radio"`: Single-choice selection from a grouped set (shared `name`).
  - `type="submit"` / `type="reset"`: Form submission and clearing controls.
- **`<select>` and `<option>`**: Dropdown lists for selecting items (e.g., cities, categories).
- **`<textarea>`**: Multi-line text input box (`rows`, `cols`).
- **`<button type="submit|reset">`**: Action triggers for form submissions.

### 6. Media & Embedded Elements
- **Images (`<img>`)**: Displays images with `src`, descriptive `alt` text, `width`, and `height`.
- **Marquee (`<marquee>`)**: Creates animated scrolling text with controls: `direction`, `scrollamount`, `bgcolor`, `loop`, `vspace`, `hspace`, `width`, and `height`.
- **Iframes (`<iframe>`)**:
  - Embeds interactive **Google Maps** with navigation pins.
  - Embeds **YouTube Videos** using responsive player iframes.
- **Video Media**: Incorporating `.mp4` video recordings.

### 7. Hyperlinks & Page Navigation
- **Internal Anchor Links**: Jumping between sections within the same page using `<a href="#section-id">` and corresponding `id="section-id"`.
- **External Links**: Linking to external resources with `<a href="https://..." target="_blank">` to open links in a new tab.
- **Top Navigation**: "Back to Top" navigation anchors (`<a href="#top">Back to Top ↑</a>`).


---

## 🐍 Other Modules Overview

In addition to HTML, this repository contains coursework and exercises in:
- **`Python_module/`**: Daily Python programming lectures and exercises (`Day3.py`, `Day4.py`, `Day5.py`, `Day6.py`).
- **`Leetcode/`**: Algorithmic problem-solving implementations (e.g., `SpacilaArray.py`).
- **`problemSolving/`**: Core logic building, conditionals, and math puzzles (`Frist.py`, `problem.py`).

---

## 🚀 How to Run Locally

You can preview any of the HTML pages in your browser:
1. Clone or download the repository:
   ```bash
   git clone https://github.com/pramodbedage/Kiran-Acadamy.git
   ```
2. Navigate into the `Html_module` folder:
   ```bash
   cd Kiran-Acadamy/Html_module
   ```
3. Open any `.html` file directly by double-clicking it, or from VS Code using **Live Server**.


1/OCT/2026

form Secation 
1. how to use the from button and the how to send value to the url and how to fech the values 
2.How to add the images and the video and audio files
3.how to add the links
4.What is user of the value ="in form uril the data is gon whit the url"
5. what is the use of the form action=" "