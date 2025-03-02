import gdown

url1 = "https://drive.google.com/file/d/1a64ptQtGw1DeNvQl1668HP9KP9uhRT_H/view?usp=drive_link"
url2 = "https://drive.google.com/file/d/1If-X5B__Yb485en_s4ey0Jwf1vmUjbYM/view?usp=drive_link"

gdown.download(url1, 'movies.pkl', quiet=False)
gdown.download(url2, 'cosine_sim.pkl', quiet=False)
