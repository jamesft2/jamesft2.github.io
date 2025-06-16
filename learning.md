---
layout: default
title: Learning
---

# Learning

This is my guide for getting up to speed on MD simulations of lipid membranes with HOOMD-blue in a way that I think is useful.
---
Try typing your name and clicking the button below:

{% raw %}
<py-script>
def greet(name):
    return f"Hello, {name}!"

def update():
    name = Element("name").value
    greeting = greet(name)
    Element("output").element.innerText = greeting


<input id="name" type="text" placeholder="Your name" />
<button py-click="update()">Greet</button>
<p id="output"></p>
{% endraw %}
