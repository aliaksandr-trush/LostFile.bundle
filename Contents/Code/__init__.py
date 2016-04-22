URL = "http://lostfilm.tv"
TITLE = 'LostFilm'

def Start():
	HTTP.Headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686; rv:32.0) Gecko/20100101 Firefox/32.0'
	Log.Info("Should be implemented")

@handler('/video/lostfilm', 'LostFilm')
def Main():
	oc = ObjectConainer(
		objects = [
			DirectoryObject(
				key = Callback(SecondMenu),
				title = 'Home Directory'
			)
		]
	)
	return oc
	Log.Info("Should be implemented")

def SecondMenu():
	oc = ObjectContainer(
		Log.Info("Implement me!")
	)
	return oc



