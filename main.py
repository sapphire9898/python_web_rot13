# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2

form="""
<form method="POST">
	<b>Enter the string to rot13:<b>
	<br>
	<textarea name="text" rows="4" cols="50">%(q)s</textarea>
	<br>
	<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
	def rot13(self, s):
	#change the string + 13; 
		res=""
		for c in s:
			if  (c >= 'a' and c < 'n') or (c >= 'A' and c < 'N'):
				res += chr(ord(c) + 13)		
			elif (c >= 'n' and c <= 'z') or (c >= 'N' and c <= 'Z'):
				res += chr(ord(c) - 13)
			else:
				res += c
		return res

	def validQ(self, text):
		dict={'>': "&gt;", '<' : "$lt;", '"' : "&quot;", '&': "&amp;"}
		for ele in dict.keys():
			text = text.replace(ele, dict[ele])
		return text
		
	def write_form(self, text=""):
		self.response.out.write(form % {"q" : text})
	def get(self):
		self.write_form()
	def post(self):
		user_q= self.rot13(self.request.get("text"))
		valid_q = self.validQ(user_q)
		self.write_form(user_q)

		
app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
