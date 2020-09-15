from registration import Session
from registration.db import User
from registration import app

class Manager:

    def register_user(self, name, fullname, nickname):
        try:
            session = Session()
            user = User()
            user_present = session.query(User).filter_by(name=name).first()
            if not user_present:
                user.name = name
                user.fullname = fullname
                user.nickname = nickname
                session.add(user)
                session.commit()
                app.logger.info('User added')
                return 'User {0} added successfully.'.format(name)
            return 'User {0} exists.'.format(name)
        except Exception as e:
            session.rollback()
            app.logger.error(str(e))
        finally:
            session.close()