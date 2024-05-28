from app import app, db, Post, Comment, Tag


def add_data():
  db.drop_all()
  db.create_all()

  post1 = Post(title='Post The First', content='Content for the first post')
  post2 = Post(title='Post The Second', content='Content for the Second post')
  post3 = Post(title='Post The Third', content='Content for the third post')

  comment1 = Comment(content='Comment for the first post', post=post1)
  comment2 = Comment(content='Comment for the second post', post=post2)
  comment3 = Comment(content='Another comment for the second post', post_id=2)
  comment4 = Comment(content='Another comment for the first post', post_id=1)

  tag1 = Tag(name='animals')
  tag2 = Tag(name='tech')
  tag3 = Tag(name='cooking')
  tag4 = Tag(name='writing')

  post1.tags.append(tag1)  # Tag the first post with 'animals'
  post1.tags.append(tag4)  # Tag the first post with 'writing'
  post3.tags.append(tag3)  # Tag the third post with 'cooking'
  post3.tags.append(tag2)  # Tag the third post with 'tech'
  post3.tags.append(tag4)  # Tag the third post with 'writing'

  db.session.add_all([post1, post2, post3])
  db.session.add_all([comment1, comment2, comment3, comment4])
  db.session.add_all([tag1, tag2, tag3, tag4])

  db.session.commit()

def add_data_2():
  life_death_post = Post(title='A post on life and death', content='life and death')
  joy_post = Post(title='A post on joy', content='joy')

  life_tag = Tag(name='life')
  death_tag = Tag(name='death')
  joy_tag = Tag(name='joy')

  life_death_post.tags.append(life_tag)
  life_death_post.tags.append(death_tag)
  joy_post.tags.append(joy_tag)

  db.session.add_all([life_death_post, joy_post, life_tag, death_tag, joy_tag])

  db.session.commit()

def show_data():
  posts = Post.query.all()

  for post in posts:
    print(post.title)
    print(post.tags)
    print('---')

  tags = Tag.query.all()
  for tag in tags:
    print(f"{tag=}")
    print(f"{tag.posts=}")


def filter_data():
  writing_tag = Tag.query.filter_by(name='writing').first()

  for post in writing_tag.posts:
    print(post.title)
    print('-' * 6)
    print(post.content)
    print('-')
    print([tag.name for tag in post.tags])
    print('-' * 20)


if __name__ == '__main__':
  with app.app_context():
    # add_data()
    # add_data_2()
    show_data()
    # filter_data()