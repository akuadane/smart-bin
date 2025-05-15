import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class WastePredictionService {
  private apiUrl = 'http://localhost:5000/predict'; // Adjust if different port

  constructor(private http: HttpClient) {}

  sendImage(image: File): Observable<any> {
    const formData = new FormData();
    formData.append('file', image);
    return this.http.post(this.apiUrl, formData);
  }
}