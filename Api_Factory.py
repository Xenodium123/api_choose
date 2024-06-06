class ApiFactory:
  @staticmethod

  def get_api(api_name):
    if api_name == 'x':
      from twitter_api import TwitterAPI
      return TwitterApi()
    elif api_name == 'github':
      from github_api import GitHubAPI
      return GitHubAPI()

    else:
      raise ValueError(f"something wrong:{api_name})
