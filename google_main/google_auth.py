import os.path
import time
from core.IO_helper import IO_Helpers 

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from passlib.hash import pbkdf2_sha256
from google.auth.exceptions import RefreshError


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly', 'https://www.googleapis.com/auth/classroom.rosters.readonly']
# https://www.googleapis.com/auth/classroom.rosters.readonly


class google_auth():

    def main_auth():
        """Shows basic usage of the Docs API.
        Prints the title of a sample document.
        """
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            try:
                creds = Credentials.from_authorized_user_file('token.json', SCOPES)
            except ValueError:
                path = os.getcwd()
                path = path + "\\" + "token.json"
                os.remove(path)
                return False
            else:
                return True
            
            
            
            # return True
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    
                    creds.refresh(Request())
                except RefreshError:
                    path = os.getcwd()
                    path = path + "\\" + "token.json"
                    os.remove(path)
                    return False
                else:
                    pass

   
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
                return True

    def get_classes():
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        try:
            service = build('classroom', 'v1', credentials=creds)
        
            results = service.courses().list(pageSize=10).execute()
            # print(results, 'res')
            courses = results.get('courses', [])
            count = 0
            classes = []
            for i in courses:
                count += 1
                name = i['name']
                id_ = i['id']
                classes.append({'number': count, 'name': name, 'id': id_})
                print('[', count,']', 'Class Name:', name)
            choice = int(IO_Helpers.single_inp("Please enter the number corrisponding to the class you want to get names from."))
            for i in classes:
                if i['number'] == choice:
                    print(i['number'])
                    print(i['name'])
                    c_id = i['id']
                    try:
                        names = []
                        student = service.courses().students().list(courseId=c_id, pageSize=10).execute()
                        hmm = student.get('students')
                        # need to add a check to make sure theres are names and not just a white space
                        for i in hmm:
                            names.append(i['profile']['name']['fullName'])
                        return names

                        
                        # students = res
                        # print(result)
                    except HttpError as err:
                        pass
           
        except HttpError as err:
            print(f"there was an error trying to authenticate your google account", {err}, "please try again")
            return False
        



# if __name__ == '__main__':
#     main()


