import twint


c = twint.Config()
c.Username = "Elon Musk"
c.Links = "include"

twint.run.Search(c)