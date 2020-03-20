from flask import Flask, render_template, request, url_for
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
import urllib.request

from web_scrapper import scrapper

labels = ["chihuahua", "japanese-spaniel", "maltese-dog", "pekinese", "shih-tzu", "blenheim-spaniel", "papillon", "toy-terrier", "rhodesian-ridgeback", "afghan-hound", "basset", "beagle", "bloodhound", "bluetick", "black-and-tan-coonhound", "walker-hound", "english-foxhound", "redbone", "borzoi", "irish-wolfhound", "italian-greyhound", "whippet", "ibizan-hound", "norwegian-elkhound", "otterhound", "saluki", "scottish-deerhound", "weimaraner", "staffordshire-bullterrier", "american-staffordshire-terrier", "bedlington-terrier", "border-terrier", "kerry-blue-terrier", "irish-terrier", "norfolk-terrier", "norwich-terrier", "yorkshire-terrier", "wire-haired-fox-terrier", "lakeland-terrier", "sealyham-terrier", "airedale-terrier", "cairn", "australian-terrier", "dandie-dinmont", "boston-bull", "miniature-schnauzer", "giant-schnauzer", "standard-schnauzer", "scotch-terrier", "tibetan-terrier", "silky-terrier", "soft-coated-wheaten-terrier", "west-highland-white-terrier", "lhasa", "flat-coated-retriever", "curly-coated-retriever", "golden-retriever",
          "labrador-retriever", "chesapeake-bay-retriever", "german-short-haired-pointer", "vizsla", "english-setter", "irish-setter", "gordon-setter", "brittany-spaniel", "clumber", "english-springer", "welsh-springer-spaniel", "cocker-spaniel", "sussex-spaniel", "irish-water-spaniel", "kuvasz", "schipperke", "groenendael", "malinois", "briard", "kelpie", "komondor", "old-english-sheepdog", "shetland-sheepdog", "collie", "border-collie", "bouvier-des-flandres", "rottweiler", "german-shepherd", "doberman", "miniature-pinscher", "greater-swiss-mountain-dog", "bernese-mountain-dog", "appenzeller", "entlebucher", "boxer", "bull-mastiff", "tibetan-mastiff", "french-bulldog", "great-dane", "saint-bernard", "eskimo-dog", "malamute", "siberian-husky", "affenpinscher", "basenji", "pug", "leonberg", "newfoundland", "great-pyrenees", "samoyed", "pomeranian", "chow", "keeshond", "brabancon-griffon", "pembroke", "cardigan", "toy-poodle", "miniature-poodle", "standard-poodle", "mexican-hairless", "dingo", "dhole", "african-hunting-dog"]


def predict_from_url():
    image = plt.imread('img.jpg')
    image = tf.image.resize(image, (224, 224))/255.0
    image = np.array(image)
    image = np.expand_dims(image, 0)

    img = model.predict(image)
    predicted = tf.squeeze(img).numpy()
    predicted_ids = np.argmax(predicted, axis=-1)
    return labels[predicted_ids]


def loadImage(url):
    urllib.request.urlretrieve(url, 'img.jpg')


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
        site_url = "https://www.akc.org/dog-breeds/{}/".format(breed)
        print("************************************************************")
        print("Site to be scraped from:", site_url)
        desc = scrapper(site_url)
        return render_template('index.html', desc=desc)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    model = tf.keras.models.load_model(
        "model.h5",
        custom_objects={'KerasLayer': hub.KerasLayer})
    print('************Model is loaded and ready to predict************')
    app.run(debug=True)
