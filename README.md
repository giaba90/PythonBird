PythonBird
==========

A Twitter tool, written in Python, by Daniele Faugiana

=============
LICENSE

This code is relased under the GPL version 3 license. See license.txt file.
License is available at http://www.gnu.org/licenses/gpl-3.0.txt

=============
EXTERNAL DEPENDANCIES

This code requires Tweepy package available at http://github.com/tweepy/tweepy.
Simply get it and paste the package in the same directory of this README.md file.
If you want to install it directly in your system using pip: 

pip install tweepy

=============
USAGE

First, you have to register an application on Twitter Developers. After registration you'll get the Consumer key and the Consumer secret. Paste them in consumer.py between quotes.

When ready, start with pythonbird.py i.e. in a bash shell, enter the same directory of this readme file and type:

python pythonbird.py

Follow the instructions. You'll get an access token and it will be automatically saved in access.py 
You don't need to repeat this authentication procedure every time you want to use Pythonbird!

=============
ISSUES

The Auth system will sometimes fail opening twitter's auth page if the browser is already opened.
Some tweets won't be saved due to carachters encoding issues. 
Code is really bad at this time, use it at your own risk. Many issues will be fixed in the next version.
It would be useful to store tweets and other data in a sqlite database; working on it.

=============
DISCLAIMER

I am not responsible for bad usage of this software, damages to systems or unlawful action.
This software is provided as is, the responsibility relies ONLY on the usage by the final user.
