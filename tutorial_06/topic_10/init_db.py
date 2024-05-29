from app import app, db, Post, Comment


def add_data():
  post1 = Post(title='Post The First', content='Content for the first post')
  post2 = Post(title='Post The Second', content='Content for the Second post')
  post3 = Post(title='Post The Third', content='Content for the third post')

  comment1 = Comment(content='Comment for the first post', post=post1)
  comment2 = Comment(content='Comment for the second post', post=post2)
  comment3 = Comment(content='Another comment for the second post', post_id=2)
  comment4 = Comment(content='Another comment for the first post', post_id=1)

  db.session.add_all([post1, post2, post3])
  db.session.add_all([comment1, comment2, comment3, comment4])

  db.session.commit()


def show_data():
  posts = Post.query.all()

  for post in posts:
    print(f'## {post.title}')
    for comment in post.comments:
      print(f'> {comment.content}')
    print('----')


if __name__ == '__main__':
  with app.app_context():
    # add_data()
    show_data()
