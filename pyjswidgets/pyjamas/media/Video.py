"""
* Copyright 2009 Mark Renouf
*
* Licensed under the Apache License, Version 2.0 (the "License"); you may not
* use this file except in compliance with the License. You may obtain a copy of
* the License at
*
* http:#www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS, WITHDIR
* WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
* License for the specific language governing permissions and limitations under
* the License.
"""

from __pyjamas__ import get_main_frame
from pyjamas.media.Media import Media
from pyjamas import DOM

"""*
* An HTML5 VIDEO element
"""
class Video(Media):

    def __init__(self, src=None, **kwargs):
        self.setElement(DOM.createElement("video"))
        if src:
            self.setSrc(src)

        Media.__init__(self, **kwargs)

    def getVideoWidth(self):
        return self.getElement().videoWidth

    def getVideoHeight(self):
        return self.getElement().videoHeight

    def setPoster(self, url):
        self.getElement().poster = url

    def getPoster(self):
        return self.getElement()

