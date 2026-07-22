import os,shutil
from pathlib import Path
def Sort(location):
   location=Path(location)
   text=location/"Text"
   image=location/"Images"
   video=location/"Videos"
   audio=location/"Audios"
   presentation=location/"Presentation"
   comFile=location/"Compressed Files"
   Program=location/"Programming Files"
   web=location/"Web Technology"
   docs=location/"Documents"
   spreadSheet=location/"Spreadsheets"
   t=0
   i=0          
   v=0
   a=0
   ps=0
   c=0
   pg=0
   w=0     
   d=0
   s=0

   if(location.exists()):
  
   
     for p in location.iterdir():
       
       if(p.suffix.lower()==".txt"):
            
            count=1
            text.mkdir(exist_ok=True)
            destination=text/p.name 
            while(destination.exists()):
                   destination = text / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
            
            shutil.move(p,destination)
            t=t+1
      
       if(p.suffix.lower() in [".png", ".jpeg", ".jpg", ".webp",".svg",".heic",".psd",".gif"]):
          count =1
          image.mkdir(exist_ok=True)
          destination=image/p.name 
          while(destination.exists()):
                   destination = image / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          i=i+1
       
       
       if(p.suffix.lower() in [".mp4",".mkv",".mov",".mpg",".avi",".webm",".3gp", ".ts",".ogv"]):
          count =1
          video.mkdir(exist_ok=True)
          destination=video/p.name 
          while(destination.exists()):
                   destination = video / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          v=v+1
       
       
       if(p.suffix.lower() in [".mp3",".wav",".ogg",".opus",".aac",".m4a"]):
          count =1
          audio.mkdir(exist_ok=True)
          destination=audio/p.name 
          while(destination.exists()):
                   destination = audio / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          a=a+1
       
       
       if(p.suffix.lower() in[".ppt",".pptx",".key",".odp"]):
          count =1
          presentation.mkdir(exist_ok=True)
          destination=presentation/p.name 
          while(destination.exists()):
                   destination = presentation / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          ps=ps+1
   
       if(p.suffix.lower() in [".zip",".rar",".tar",".gz",".xz",".iso"]):
          count =1
          comFile.mkdir(exist_ok=True)
          destination=comFile/p.name 
          while(destination.exists()):
                   destination = comFile / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          c=c+1
   
       if(p.suffix.lower() in  [".py",".c",".cpp",".pyw",".java"]):
          count =1
          Program.mkdir(exist_ok=True)
          destination=Program/p.name 
          while(destination.exists()):
                   destination = Program / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          pg=pg+1

       if(p.suffix.lower() in [".html",".css",".js",".jsx",".tsx",".php",".jsp",".asp",".php",".jsp",".xml"]):
          count =1
          web.mkdir(exist_ok=True)
          destination=web/p.name 
          while(destination.exists()):
                   destination = web / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          w=w+1

       if(p.suffix.lower() in [".pdf",".doc",".docx",".rtf",".pages"]):
          count =1
          docs.mkdir(exist_ok=True)
          destination=docs/p.name 
          while(destination.exists()):
                   destination = docs / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          d=d+1  
     
     
       if(p.suffix.lower() in [".xls",".xlsx",".csv",".tsv"]):
          count =1
          spreadSheet.mkdir(exist_ok=True)
          destination=spreadSheet/p.name 
          while(destination.exists()):
                   destination = spreadSheet / f"{p.stem} ({count}){p.suffix}"
                   count=count+1
          shutil.move(p,destination)
          s=s+1

     return{ 
             "success":True,      
               "text":t,
               "image":i,
               "video":v,
               "audio":a,
               "presentation":ps,
               "compressed":c,
               "programme":pg,
               "web":w,
               "document":d,
               "spreadsheet":s






            }







   else:
    return {
         "success": False,
         "message":"Please Enter a valid Path"
    }

