## Welcome to FjordFish. 
### The North Atlantic marine faunal computer vision dataset as part of the publication "Annotation strategy trade-offs for deep learning-based underwater fish detection".

![corkwing wrasse](https://github.com/jdavidpoling/FjordFish/blob/main/Images/1407.jpg)

This is a dataset of imagery from baited and unbaited remote underwater video from the Norwegian and Swedish North Atlantic coastlines and acts as a dataset for computer vision model training as well as testing, validation and pretraining.

The dataset contain approximately 6000 annotations across 3000 images from wild fauna (table 1), as well as images of coastal cod gadus _morhua_ of varied sizes and ages from a semi-natural mesocosm resembling wild rocky habitat.

### Detection and Classification

The dataset contains 28 classes:
  - 23 species level classes i.e. "cod" (gadus _morhua_)
  - 5 uknown or group level classes i.e. "labrids_unknown" (unknown wrasses)

All annotations are bounding boxes contained in text files currently in the You Only Look Once (YOLO) format for YOLOv8+

|Class ID|Class Name|Common Name|Latin Name|Species Group|Total Annotations|
|---|---|---|---|---|---|
|0|ballan|Ballan Wrasse|_Labrus berygylta_|Labrids|93|
|1|cuckoo_female|Cuckoo Wrasse Female|_Labrus mixtus_|Labrids|47|
|2|cuckoo_male|Cuckoo Wrasse Male|_Labrus mixtus_|Labrids|31|
|3|corkwing_female|Corkwing Wrasse Female|_Symphodus melops_|Labrids|456|
|4|corkwing_male|Corkwing Wrasse Male|_Symphodus melops_|Labrids|1215|
|5|goldsinny|Goldsinny Wrasse|_Ctenolabrus rupestris_|Labrids|152|
|6|rock_cook|Rock Cook/Small-mouthed Wrasse|_Ctenolabrus exoletus_|Labrids|152|
|7|labrids_unknown|Labrids Unknown|_Labridae sp._|Labrids|333|
|8|cod|Atlantic Cod|_Gadus morhua_|Gadids|811|
|9|cod_yoy|Atlantic Cod Young of the Year|_Gadus morhua_|Gadids|181|
|10|haddock|Haddock|_Melanogrammus aeglefinus_|Gadids|7|
|11|pollack|Pollack|_Pollachius pollachius_|Gadids|149|
|12|poor_cod|Poor Cod|_Trisopterus minutus_|Gadids|22|
|13|saithe|Saithe|_Pollachius virens_|Gadids|39|
|14|whiting|Whiting|_Melangius melangus_|Gadids|101|
|15|gadids_unknown|Gadids Unknown|_Gadidae sp._|Gadids|200|
|16|spiny_dogfish|Spiny Dogfish|_Squalus acanthias_|Sharks|684|
|17|sharks_unknown|Sharks Unknown|_Squaliformes sp._|Sharks|0|
|18|brown_crab|Brown Crab|_Cancer pagurus_|Decapods|190|
|19|green_crab|Green Crab|_Carcinus maenas_|Decapods|38|
|20|hermit|Hermit Crab|_Paguridae sp._|Decapods|15|
|21|lobster|European Lobster|_Homarus gammarus_|Decpods|1|
|22|decapods_unknown|Decapods Unknown|_Decapoda sp._|Decapods|5|
|23|ling|Ling|_Molva molva_|none|30|
|24|two_spot_goby|Two Spot Goby|_Pomatoschistus flavenscens_|none|113|
|25|black_goby|Black Goby|_Gobius niger_|none|1|
|26|sand_goby|Sand Goby|_Pomatoschistus minutus_|none|3|

### Download
https://zenodo.org/records/17950781

### Models
If you are looking for the final trained YOLOv9c models from the publication, they can be found here: https://huggingface.co/collections/jdpoling/fjordfish-yolo9c

## Citation
If you use the FjordFish dataset in your work, please cite the associated paper:
```
Poling, J. D., Perry, D., Halvorsen, K. T., Malde, K., Thormar, J., Larsen, T., & Sørdalen, T. K. (2026). Annotation strategy trade-offs for deep learning-based underwater fish detection. Ecological Informatics, 103891.
```
