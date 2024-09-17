# How internet works
- Our computer (unique IP address) <> ISP <> Server of some website address we want to use (unique IP address)
- Information transmitted between our PC --> ISP --> Server and back, based on (unique IP address)
- Our PC store cache copy of a local version of the website (related to prank)
- World connected via under sea cables
https://www.submarinecablemap.com/
![alt text](image-1.png)

# How website works
Components
- HTML = structure
- CSS = beauty
- JS = function

![alt text](image.png)

- Prank demo
![alt text](image-2.png)
![alt text](image-3.png)

this is possile because the local cache of website on our computer, at refresh --> returns to original codings.


## HTML
HTML tags:
![alt text](image-4.png)

### HTML heading elements
![alt text](image-5.png)

### Void elements
#### Horizontal rule element
![alt text](image-6.png)
![alt text](image-7.png)

### Break element
![alt text](image-8.png)
![alt text](image-9.png)


### HTML boilerplate
![alt text](image-10.png)

- Indenting is important for readability
- There can be more in <head></head>
- Main content of website is in the <body></body>

### List elements

#### Unordered list
![alt text](image-12.png)

#### Ordered list
![alt text](image-13.png)

### Nesting and indentation
![alt text](image-14.png)

### Anchor elements
[Anchor Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a)


![Single attribute](image-15.png)
![Many attributes](image-16.png)

![alt text](image-17.png)

### Image elements
It is a void element, no closing tag
![alt text](image-18.png)
![alt text](image-19.png) 
* the 200 = size of photo
* the alt text = help read out loud for accessability for people who cannot see the website

## CSS

### How to add CSS to HTML website


- Inline
![alt text](image-20.png)

- Internal
![alt text](image-21.png)

- External (mostly used)
![alt text](image-22.png)

### CSS selectors

```css
h1 {
  color: "red"
}
/* In this case the h1 is CSS selector, it will make all Header1 to have this format */
```

### Class selectors

```css
.red-heading {
  color: "red"
}
/* After dot, name of class*/

<h2 class = "red-heading">Red</h2>
<h2>This will not be red-ed</h2>

```

### ID selectors 

```css
#id_something {
  color: "red"
}
/* After #, name of ID*/

<h2 id = "id_something">Red</h2>
<h2>This will not be red-ed</h2>

```

Difference between ID vs Class --> applied on 1 vs many elements.

### Attribute selectors

```css
html_element[attribute] {
  color: "red"
}
/* After dot, name of class*/

<h2 class = "red-heading">Red</h2>
<h2>This will not be red-ed</h2>

```

![alt text](image-28.png)
![alt text](image-29.png)