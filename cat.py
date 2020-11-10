import os
import flickrapi
import urllib
import key

path = os.getcwd()
# Flickr api access key 

flickr=flickrapi.FlickrAPI(key.api_key, key.api_secret, cache=True)


keyword = 'cute cats'

photos = flickr.walk(text=keyword,
                     tag_mode='all',
                     tags=keyword,
                     extras='url_c',
                     per_page=100,           # may be you can try different numbers..
                     sort='relevance')

urls = []
for i, photo in enumerate(photos):
    url = photo.get('url_c')
    urls.append(url)
    
    # get 50 urls
    if i > 50:
        break

#make a directory for cats and dogs
if not os.path.isdir(path + '/cats'):
    os.mkdir(path + '/cats')

# Download image from the url and save it to '00001.jpg'
for i in range(len(urls)):
    if urls[i]!=None:
        urllib.request.urlretrieve(urls[i], path + '/cats/' + '0000' +str(i)+'.jpg')


