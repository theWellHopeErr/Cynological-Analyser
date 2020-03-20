import requests
from bs4 import BeautifulSoup

labels = ["chihuahua", "japanese-spaniel", "maltese-dog", "pekinese", "shih-tzu", "blenheim-spaniel", "papillon", "toy-terrier", "rhodesian-ridgeback", "afghan-hound", "basset", "beagle", "bloodhound", "bluetick", "black-and-tan-coonhound", "walker-hound", "english-foxhound", "redbone", "borzoi", "irish-wolfhound", "italian-greyhound", "whippet", "ibizan-hound", "norwegian-elkhound", "otterhound", "saluki", "scottish-deerhound", "weimaraner", "staffordshire-bullterrier", "american-staffordshire-terrier", "bedlington-terrier", "border-terrier", "kerry-blue-terrier", "irish-terrier", "norfolk-terrier", "norwich-terrier", "yorkshire-terrier", "wire-haired-fox-terrier", "lakeland-terrier", "sealyham-terrier", "airedale-terrier", "cairn", "australian-terrier", "dandie-dinmont", "boston-bull", "miniature-schnauzer", "giant-schnauzer", "standard-schnauzer", "scotch-terrier", "tibetan-terrier", "silky-terrier", "soft-coated-wheaten-terrier", "west-highland-white-terrier", "lhasa", "flat-coated-retriever", "curly-coated-retriever", "golden-retriever",
          "labrador-retriever", "chesapeake-bay-retriever", "german-short-haired-pointer", "vizsla", "english-setter", "irish-setter", "gordon-setter", "brittany-spaniel", "clumber", "english-springer", "welsh-springer-spaniel", "cocker-spaniel", "sussex-spaniel", "irish-water-spaniel", "kuvasz", "schipperke", "groenendael", "malinois", "briard", "kelpie", "komondor", "old-english-sheepdog", "shetland-sheepdog", "collie", "border-collie", "bouvier-des-flandres", "rottweiler", "german-shepherd", "doberman", "miniature-pinscher", "greater-swiss-mountain-dog", "bernese-mountain-dog", "appenzeller", "entlebucher", "boxer", "bull-mastiff", "tibetan-mastiff", "french-bulldog", "great-dane", "saint-bernard", "eskimo-dog", "malamute", "siberian-husky", "affenpinscher", "basenji", "pug", "leonberg", "newfoundland", "great-pyrenees", "samoyed", "pomeranian", "chow", "keeshond", "brabancon-griffon", "pembroke", "cardigan", "toy-poodle", "miniature-poodle", "standard-poodle", "mexican-hairless", "dingo", "dhole", "african-hunting-dog"]
wlabels = []
nwlabels = []
count = 0
for i in labels:
  url = "https://www.akc.org/dog-breeds/{}/".format(i)
  resp = requests.get(url)
  if resp.status_code == 200:
    count+=1
    wlabels.append(i)
    print("Successfully opened the page: {}".format(count))
  else:
    nwlabels.append(i)
# print(nwlabels)
print(wlabels)
print(len(nwlabels))