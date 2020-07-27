import requests

projects = [
  {
    "title": "Rick and Morty characters",
    "description": "List of Rick and Morty characters",
    "image": "https://previews.dropbox.com/p/thumb/AA26ohhJdloNFHVwjHaCrPUkG9NrD0PFpBx6CnZOxGEgFeP0PxUXV8oHKCXfFQxL1EFIUrIsh9-Ke6DpsxGJrV-QX62dBFvjMA0_6Q5WDiqGIq804OzvDn_PN5hzvOIwWbdICZ5eZ05jIxNYH5UyXfDo2T7NPrSPSjpuru50_hSxs0Br4c0Yl-WLoA_0XC4hwHTn8PMki266bxT8yUKkN6MzjJQa9w5WnAoHPV2kbDkY-5GjNhf3d2BmzVpZPVvPahsiMbZh37pFKspGgvoBUr63oZGcLpYal9ZzjW7DA-oSI0T0VCIol1UXf7wJ3TUykTAWOac--eF73_PiL40oCMZtSMTwnuTAHQjLlKJ34dxeXg/p.png?fv_content=true&size_mode=5",
    "url": "https://rick-morty-characters.netlify.app/",
    "tec": "Vanilla Js"
  },
  {
    "title": "Pokedex-Web-Scraping",
    "description": "Web secraper with puppeteer to get the firt generacion of pokemons",
    "image": "https://previews.dropbox.com/p/thumb/AA3hKxrZr9O4cuZFsdEMz1Y8M2YQV0oGid-NBSBDK2Zr15k_WJBD-bstrKGrXEFsOVfqijuo4oicsTKYw_rLOm1Qwx-3Ujdyb_7_gOqi1q3eVlU5VKuPnCrQovzW344OH9BE4XfhsOH8v2h-RvUX0xfbsZUydQS3PSmt4Y5xnjYVz86z_WNN66Omdho4t5yJzf5SsWwj_Ex3IDV8HLgqPUyKtFrPI6LlyInnt3G4laISJ-xkLAO63IIqnvcUSv8lxlRi5nKPboxCM4b952sLhYqm3q26xWycNOPF_5bjSmEdI_89D58-uPiwY19q3GfmqwdsKd-0RQzKLEweMzsOvqChzzZcqjST-e46hm2TNnp5cg/p.png?fv_content=true&size_mode=5",
    "url": "https://github.com/sd8956/Pokedex-Web-Scraping",
    "tec": "JavaScript React"
  },
  {
    "title": "Covid19-data",
    "description": "Informacion about Covid-19 per country",
    "image": "https://previews.dropbox.com/p/thumb/AA3yBMYwsGV_imIV-BH0LRtiHEIz0PuJUbeRMi-jTUzWONmEBytl4mo1eQhyhlQcKqM4arLnkGNEsY2svIW0F19soIZwIyIWDebrI2REsI8_kfFhmvh73kXIevzot-mnOjwnFNp_3MecjGXRc_YrZebWaKw-1hRHwXr13m2QN3IQZaDAF1YdzEmXbQ22pjRaI_E3ahEi95Oxyk3Zvvis312asctN50M5lVCmPoLU_UvG6qUek0yedyHAnJmN0c1tmZ-ix9y3NdIrZTua9OpVK7WFhddDN86zd9DUbAcRnXSmgzQoBSCx-dSBHGRRwvNJZ5G1fzAM7xofd7tds1QEvHOInJcuF_s8H4OeMhkBEA0TGg/p.png?fv_content=true&size_mode=5",
    "url": "https://data-vs-cv19.netlify.app/",
    "tec": "JavaScript React"
  },
  {
    "title": "Pinterest clone",
    "description": "Informacion about Covid-19 per country",
    "image": "https://previews.dropbox.com/p/thumb/AA1aHac9kajC-U-eVycEGx5W-La6gLM3HEvUkNgPk1QaSFt3nR7DaFjazZSZ1IAbyoc9Z1hptpq9pCoWw2Z96SUgxhBDmuW1xH2IC1T3Ed7scUOZKBR8BBhzztexjl9BTzMb1j1vyqrSbVRAf2QLyOA6qTNh1OCtoJQmHVSCP6pZEBu-GuuxEJT2sqcXkycGuQcsQfQtomimKh_rwnPVM-6OH84H0ipqbOf-8lKH6SlIZY-p9OqdCR2APORzkQr_B1KeKqYl93kW3_CT0QVu6IXHHoMlQbeCEg_2ehy0gRZAbO8JmY9l9SL98ReFfLj9Mj4PphKNUlAJNEJVa1kjTf0Dg7GYfo_l50qynvQvGBBfyg/p.png?fv_content=true&size_mode=5",
    "url": "https://github.com/sd8956/pinterest-clone",
    "tec": "Python Django"
  },
  {
    "title": "Bot twitter",
    "description": "Publish a random tweet every 2 hours",
    "image": "https://previews.dropbox.com/p/thumb/AA2tNwYuwRAYeUO-eTXHay5Y5_OcrVBtGOGvgcJGf4c_VT8kqlP5q-1Xdgs0iUG6NhUIOzf7nRHUnOSWTh2StloORC2tLgUNTdW-ORP_-qKPhaYQxetfe_yrNv45IPWRTSJhvyzJUNUTGDYUpn-0CTQhC5cfWRrvzkICd4ud4Z0Mrs7d_zi2DZjBia-rSrKfBRM-JznEYXy4_lq9kU4zxQ7RsyK5__LhG__jnZAzJOMEYPCUZL6cyTspyZcBK3vIm3sLGpsr3l5mYUg18zpLKdExxhvH6opWURm1EpnklvcHS-azTSWpqia7at76l-qqnf-oA2PLqQLgPzEpIrbk48YouQK21tytj-8noFDADJwqTQ/p.png?fv_content=true&size_mode=5",
    "url": "https://github.com/sd8956/bot_twitter",
    "tec": "Python Celery"
  },
  {
    "title": "Form to publish a tweet",
    "description": "Publish tweets with a form",
    "image": "https://previews.dropbox.com/p/thumb/AA2Ibi2S38Xx52kllImzxzBRmygjjRtzuUuxS0au08_Ho0TiWRfsnGzW2ZTCdmShg9a0mLyfEWKp2vDbU1BW2PodqtywBzxIBGs6C-JeHNoWMVmRen0pVeMHH0Dqs8dIExzWxhCcTE7SsglfcqEUF5kqeB3ADIMUU-P2IhB6PAWJf7GUDoTD3qs0RC77CIMW0mXQ6Hkf2_pZh-Kx0f_Hl6rgZmG7Zfjdeu7J4IBMgxF1KjxPkl3X6wp77sD86Tx-2rKmAj2K_tOJigYXA7xd9MY0HQaT2JDmq_ezZgSRWFcDpXxMl_EOW1yW74-h7RG2GikesWHIVoguI4DdkC5Jn04cyxQAk-V0wRuriUKsH-pxjA/p.png?fv_content=true&size_mode=5",
    "url": "https://github.com/sd8956/form_tweet",
    "tec": "Python Flask Celery"
  }
]

def run():
  for project in projects:
    requests.post('http://127.0.0.1:8000/projects', json={
      "title": project['title'],
      "description": project['description'],
      "image": project['image'],
      "url": project['url'],
      "tec": project['tec']
    })

if __name__ == "__main__":
    run()