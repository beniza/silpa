# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2010 Santhosh Thottingal <santhosh.thottingal@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

import sys
import re
import os
import uuid
from common import *
from utils import *
class TTS(SilpaModule):
    def __init__(self):
        self.template=os.path.join(os.path.dirname(__file__), "tts.html")
        
    def set_request(self,request):
        self.request=request
        self.speech = self.request.get('speech')
        self.text = self.request.get('text')
        
    def is_self_serve(self) :       
        if self.speech or self.text:
            return True
        else:
            return False
                    
                    

    def get_mimetype(self):
        if self.speech:
            return "audio/ogg"
                                
    def serve(self):                            
        if self.speech:
            return codecs.open(os.path.join("/tmp",self.speech)).read()
                
                                                
    @ServiceMethod  
    def text_to_ogg(self,text) :
        tempInfileName = os.path.join("/tmp","tempInfile")
        tempInfile = open(tempInfileName, "w")  
        tempInfile.write(text.encode("utf-8"))
        tempInfile.close()  
        filename= str(uuid.uuid1())[0:5]
        speechfile = os.path.join("/tmp",filename+".ogg")
        cmd = "dhvani  "+ tempInfileName + " -o "+ speechfile
        os.system(cmd)
        return "?speech="+filename+".ogg"
        
    def get_module_name(self):
        return "Text to speech"
    def get_info(self):
        return  "Converts text in Indian languages to speech"    
        
def getInstance():
    return TTS()

