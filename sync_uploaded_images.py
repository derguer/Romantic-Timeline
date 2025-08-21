#!/usr/bin/env python3
"""
Sync Uploaded Images Script
Überwacht localStorage und synchronisiert hochgeladene Bilder zu GitHub
"""

import os
import json
import base64
import hashlib
import subprocess
from datetime import datetime
from PIL import Image
import io

def extract_images_from_browser_storage():
    """
    Extrahiert Bilder aus dem localStorage-Format und speichert sie im images/ Ordner
    """
    print("🔍 Suche nach hochgeladenen Bildern...")
    
    # Hier würdest du normalerweise localStorage auslesen
    # Da das nur im Browser möglich ist, simulieren wir es
    print("ℹ️  Hinweis: Dieses Script muss erweitert werden um localStorage auszulesen")
    print("💡 Alternative: Drag & Drop Ordner für neue Bilder")
    
    return []

def process_new_image(image_path, target_name=None):
    """
    Verarbeitet ein neues Bild und fügt es zum images/ Ordner hinzu
    """
    try:
        # Öffne und optimiere das Bild
        with Image.open(image_path) as img:
            # Konvertiere zu RGB falls nötig
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
            
            # Komprimiere wenn zu groß
            if img.width > 1920 or img.height > 1920:
                img.thumbnail((1920, 1920), Image.Resampling.LANCZOS)
            
            # Generiere eindeutigen Namen
            if not target_name:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                hash_obj = hashlib.md5(open(image_path, 'rb').read())
                file_hash = hash_obj.hexdigest()[:8]
                target_name = f"uploaded_{timestamp}_{file_hash}.jpeg"
            
            # Speichere im images/ Ordner
            target_path = os.path.join("images", target_name)
            img.save(target_path, "JPEG", quality=85, optimize=True)
            
            print(f"✅ Bild gespeichert: {target_path}")
            return target_path
            
    except Exception as e:
        print(f"❌ Fehler beim Verarbeiten von {image_path}: {e}")
        return None

def sync_to_github():
    """
    Synchronisiert neue Bilder zu GitHub - DISABLED
    """
    print("🚫 GitHub sync DISABLED - Manual updates only")
    print("ℹ️  Bilder werden nur lokal verarbeitet")
    # subprocess.run(['git', 'add', 'images/'], check=True)
    # subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
    # subprocess.run(['git', 'push'], check=True)

def watch_upload_folder():
    """
    Überwacht einen Upload-Ordner für neue Bilder
    """
    upload_folder = "uploads"
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
        print(f"📁 Upload-Ordner erstellt: {upload_folder}/")
        print("💡 Lege neue Bilder hier hinein zum Synchronisieren")
    
    # Prüfe auf neue Bilder
    image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
    new_images = []
    
    for filename in os.listdir(upload_folder):
        if filename.endswith(image_extensions):
            file_path = os.path.join(upload_folder, filename)
            new_images.append(file_path)
    
    if new_images:
        print(f"🆕 {len(new_images)} neue Bilder gefunden:")
        for img_path in new_images:
            print(f"  📷 {os.path.basename(img_path)}")
            
            # Verarbeite das Bild
            processed_path = process_new_image(img_path)
            
            if processed_path:
                # Lösche Original aus Upload-Ordner
                os.remove(img_path)
                print(f"🗑️  Original gelöscht: {img_path}")
        
        # Synchronisiere zu GitHub
        sync_to_github()
    
    return len(new_images)

if __name__ == "__main__":
    print("🚀 Romantic Timeline - Image Sync Script")
    print("=" * 50)
    
    # Erstelle Upload-Ordner falls nicht vorhanden
    processed_count = watch_upload_folder()
    
    if processed_count == 0:
        print("\n💡 So verwendest du das Script:")
        print("1. Lege neue Bilder in den 'uploads/' Ordner")
        print("2. Führe dieses Script aus: python3 sync_uploaded_images.py")
        print("3. Bilder werden automatisch verarbeitet und zu GitHub hochgeladen")
        print("\n🔄 Oder führe es regelmäßig aus um kontinuierlich zu synchronisieren")
