import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent }  from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { ContentComponent } from './components/content/content.component';
import { FooterComponent } from './components/footer/footer.component';

import { HomePage } from './pages/home/home.component';

@NgModule({
  imports:      [
    BrowserModule,
    AppRoutingModule,
  ],
  declarations: [
    AppComponent,
    HeaderComponent,
    ContentComponent,
    FooterComponent,
    HomePage,
  ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }
