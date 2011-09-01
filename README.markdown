A Wiki-based CMS, written as a research of concepts of tags and categorization.

Traditionally, a URL indicates a path in a website hierarchy. In contrast, nord-engine considers it to be a set of (unordered) tags joined by slash (a tag-set). 

E.g. a link pointing to one's private library catalog "http://site/private/library" can be thought as a link to a page with two tags: "private" and "library". Therefore, the same page can be accessed by another URL: "http://site/library/private". That seems to be logical. Furthermore, public library catalog can be bound to tags "public" and "library".

Accessing a tag-set bound to several pages (i.e. "http://site/library") as an authorized user leads to an index of all pages available:

 * /library/private
 * /library/public

nord-engine features Creole wiki markup, TLS authentication and a flexible extensions mechanism. The patch located in misc/ repository implements [TLS SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) and TLS client auth for lighttpd web server.

nord-engine depends on:

 * [Creoleparser](http://code.google.com/p/creoleparser)
 * [Python Google Chart](http://pygooglechart.slowchop.com)
 * [django-google-analytics](http://code.google.com/p/django-google-analytics)
 * [sslauth](http://code.google.com/p/sslauth)
 * [django-tagging](http://code.google.com/p/django-tagging/)
