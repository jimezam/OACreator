from src.oa.converters.Converter import Converter

import logging
from markdown_it import MarkdownIt
# from mdit_py_plugins.front_matter import front_matter_plugin
# from mdit_py_plugins.footnote import footnote_plugin

logger = logging.getLogger('root')

# TODO: https://wiki.python.org/moin/reStructuredText

class ConverterMarkdown2HTML (Converter):

    def __init__(self, contents):
        super().__init__(contents)

    def convert(self):
        # TODO: improve tags support (plugins)
        
        md = (
            MarkdownIt()
#            .use(front_matter_plugin)
#            .use(footnote_plugin)
#            .disable('image')
#            .enable('table')
        )

        # tokens = md.parse(self.contents)
        
        return md.render(self.contents)