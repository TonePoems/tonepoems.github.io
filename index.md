# Hello World

This is my personal website, for anything I want it to be.

### About Me
I'm a software engineer, recently (2025) graduated with my Masters in Computer Science. I've been in the defense industry since 2021, but for more boring work stuff see my rarely updated [LinkedIn](https://www.linkedin.com/in/anthony-mitchell-3b01b8158/) or [résumé](resources/resume.pdf).

### About this Site
As mentioned, this site is for my personal ramblings, interesting projects I want to document, maybe some book reviews, and other things I find important. I've been inspired for by the idea of a [personal website](https://localghost.dev/blog/this-page-is-under-construction/) and [digital gardening](https://anhvn.com/garden/digital-gardening/) for a while, and am finally giving it a go. No promises, including to myself. 

I'll get to it when I get to it, and that is fine. 

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
