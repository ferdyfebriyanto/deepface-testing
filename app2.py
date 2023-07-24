from deepface import DeepFace
import pandas as pd
import time

def deepface_test(image1, image2, model, metric, be):
  now = time.time()
  df = DeepFace.verify(img1_path=image1, img2_path=image2, model_name=model, distance_metric=metric, enforce_detection=False, detector_backend=be)
  end = time.time()
  df['time'] = end - now
  return df

photo = ["ferdy.jpg", "laudry.jpg", "rizal.jpg"]
model = "ArcFace"
detectorBE = "mtcnn"
metric = "cosine"

for i in range(3):
  selectPhoto = photo[i]
  data = []
  
  for i in range(15):
    img = 1 + i
    imageName = str(img) + ".jpg"
    
    image1 = selectPhoto
    image2 = "dataset/ferdy/normal/" + imageName
    print(image2)
    
    result = deepface_test(image1=image1, image2=image2, model=model, metric=metric, be= detectorBE)
    obj = {
      "verified": result['verified'],
      "distance": result['distance'],
      "threshold": result['threshold'],
      "model": result['model'],
      "detector": result['detector_backend'],
      "similarity_metric": result['similarity_metric'],
      "time": result['time']
    }
    
    data.append(obj)
  
  df = pd.DataFrame(data)
  namaExcel = selectPhoto + "_" + model + "_" + detectorBE + "_" + metric + ".xlsx"
  sheetName = 'DataSheet'

  df.to_excel(namaExcel, sheet_name=sheetName, index=False)
  
print("done")