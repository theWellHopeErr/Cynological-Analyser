from flask import Flask, render_template, request, url_for
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

from web_scrapper import scrapper

labels = ["chihuahua", "japanese-chin", "maltese", "pekingese", "shih-tzu", "cavalier-king-charles-spaniel", "papillon", "toy-fox-terrier", "rhodesian-ridgeback", "afghan-hound", "basset-hound", "beagle", "bloodhound", "bluetick-coonhound", "black-and-tan-coonhound", "treeing-walker-coonhound", "english-foxhound", "redbone-coonhound", "borzoi", "irish-wolfhound", "italian-greyhound", "whippet", "ibizan-hound", "norwegian-elkhound", "otterhound", "saluki", "scottish-deerhound", "weimaraner", "staffordshire-bull-terrier", "american-staffordshire-terrier", "bedlington-terrier", "border-terrier", "kerry-blue-terrier", "irish-terrier", "norfolk-terrier", "norwich-terrier", "yorkshire-terrier", "wire-fox-terrier", "lakeland-terrier", "sealyham-terrier", "airedale-terrier", "cairn-terrier", "australian-terrier", "dandie-dinmont-terrier", "boston-terrier", "miniature-schnauzer", "giant-schnauzer", "standard-schnauzer", "scottish-terrier", "tibetan-terrier", "silky-terrier", "soft-coated-wheaten-terrier", "west-highland-white-terrier", "lhasa", "flat-coated-retriever", "curly-coated-retriever", "golden-retriever", "labrador-retriever", 
          "chesapeake-bay-retriever", "german-shorthaired-pointer", "vizsla", "english-setter", "irish-setter", "gordon-setter", "brittany", "clumber-spaniel", "english-springer-spaniel", "welsh-springer-spaniel", "cocker-spaniel", "sussex-spaniel", "irish-water-spaniel", "kuvasz", "schipperke", "belgian-sheepdog", "belgian-malinois", "briard", "australian-kelpie", "komondor", "old-english-sheepdog", "shetland-sheepdog", "collie", "border-collie", "bouvier-des-flandres", "rottweiler", "german-shepherd", "doberman-pinscher", "miniature-pinscher", "greater-swiss-mountain-dog", "bernese-mountain-dog", "appenzeller-sennenhund", "entlebucher-mountain-dog", "boxer", "bullmastiff", "tibetan-mastiff", "french-bulldog", "great-dane", "st-bernard", "american-eskimo-dog", "alaskan-malamute", "siberian-husky", "affenpinscher", "basenji", "pug", "leonberger", "newfoundland", "great-pyrenees", "samoyed", "pomeranian", "chow-chow", "keeshond", "brussels-griffon", "pembroke-welsh-corgi", "cardigan-welsh-corgi", "poodle-toy", "poodle-miniature", "poodle-standard", "xoloitzcuintli", "Dingo", "Dhole", "African Wild Dog"]

def predict_from_url():
    image = plt.imread('static/img/img.jpg')
    image = tf.image.resize(image, (224, 224))/255.0
    image = np.array(image)
    image = np.expand_dims(image, 0)

    img = model.predict(image)
    predicted = tf.squeeze(img).numpy()
    predicted_ids = np.argmax(predicted, axis=-1)
    return labels[predicted_ids]


def loadImage(url):
    urllib.request.urlretrieve(url, 'static/img/img.jpg')


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            return render_template('index.html', isURLNotWorking=True)
        loadImage(url)
        breed = predict_from_url()
        print("************************************************************")
        print("Predicted Breed: ", breed)
        if breed in ["Dingo", "Dhole", "African Wild Dog"]:
            return render_template('index.html', breed=breed, image_url = url )
        site_url = "https://www.akc.org/dog-breeds/{}/".format(breed)
        print("************************************************************")
        print("Site to be scraped from:", site_url)
        desc = scrapper(site_url)
        return render_template('index.html', desc=desc, image_url = url )
    else:
        return render_template('index.html')


if __name__ == '__main__':
    model = tf.keras.models.load_model(
        "model.h5",
        custom_objects={'KerasLayer': hub.KerasLayer})
    print('************Model is loaded and ready to predict************')
    app.run(debug=True)
