{% if latest_story_list %}
<h1>{{ story.heading }}</h1>
    <ul>
    {% for story in latest_story_list %}
        <li><a href="/Newz/{{ story.id }}/">{{ story.storyTxt }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No stories are available.</p>
{% endif %}