def parse_manifold_data(poet, poet_id):
  attributes = {attr['trait_type']: attr['value'] for attr in poet.get('attributes', [])}
  
  poet_metadata = {
      "poet_id": poet_id,
      "name": poet.get("name"),
      #"description": poet.get("description"),
      "rewrites": poet.get("rewrites"),
      "image": poet.get("image"),
      #"image_url": poet.get("image_url"),
      #"thumbnail_url": poet.get("thumbnail_url"),
      "class": attributes.get("class"),
      "origin": attributes.get("origin"),
      "latent": attributes.get("latent"),
      "prime": attributes.get("prime"),
      "influence": attributes.get("influence"),
      "words": attributes.get("words"),
      "lexicon": attributes.get("lexicon")
  }
  
  return poet_metadata
