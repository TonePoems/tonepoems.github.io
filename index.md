# Hello World

This is my personal website, for anything I want it to be.

### About Me
I'm a software engineer, recently (2025) graduated with my Masters in Computer Science. I've been in the defense industry since 2021, but for more boring work stuff see my rarely updated [LinkedIn](https://www.linkedin.com/in/anthony-mitchell-3b01b8158/).

### About this Site
As mentioned, this site is for my personal ramblings, interesting projects I want to document, maybe some book reviews, and other things I find important. I've been inspired for a while by the ide of a [personal website](https://localghost.dev/blog/this-page-is-under-construction/) and [digital gardening](https://anhvn.com/garden/digital-gardening/) for a while, so want to give it a go. No promises, including to myself. I'll get to it when I get to it, and that is fine. 

- [Cool Projects](pages/cool_projects.md)


### Posts
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>


### Sorted by Tag

Here is a list of all tags used across my posts.

{% for tag in site.tags %}
  <h2>{{ tag[0] }}</h2>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}


{% include footer.html %}
