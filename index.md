layout: page
title: "Main Page"
permalink: /index

# Hello World

This is my website

### About Me


### About this Site


- [Cool Projects](pages/cool_projects.md)



### Posts
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>


{% include footer.html %}
