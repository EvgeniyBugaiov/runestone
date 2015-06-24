# Copyright (C) 2011  Bradley N. Miller
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
__author__ = 'isaacdontjelindell'

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive


DISQUS_LINK = """\
<div id="disqus_thread"></div>
<script type="text/javascript">
    /* * * CONFIGURATION VARIABLES * * */
    var disqus_shortname = 'alialiev';
    
    /* * * DON'T EDIT BELOW THIS LINE * * */
    (function() {
        var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/embed.js';
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
"""


def setup(app):
    app.add_directive('disqus', DisqusDirective)
    
    app.add_node(DisqusNode, html=(visit_disqus_node, depart_disqus_node))
    app.connect('doctree-resolved' ,process_disqus_nodes)
    app.connect('env-purge-doc', purge_disqus_nodes)

class DisqusNode(nodes.General, nodes.Element):
    def __init__(self,content):
        super(DisqusNode,self).__init__()
        self.disqus_components = content


def visit_disqus_node(self, node):
    res = DISQUS_LINK

    res = res

    self.body.append(res)

def depart_disqus_node(self,node):
    pass

def process_disqus_nodes(app, env, docname):
    pass

def purge_disqus_nodes(app, env, docname):
    pass


class DisqusDirective(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False
    option_spec = {}


    def run(self):
        """
        generate html to include Disqus box.
        :param self:
        :return:
        """

        return [DisqusNode(self.options)]

