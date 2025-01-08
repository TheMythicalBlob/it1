const språkData = {
  norsk: {
    tittel:
      "Påvirker et stort digitalt fotavtrykk individers personvern, og medfører dette farer?",
    innhold:
      "Et stort digitalt fotavtrykk kan utgjøre en risiko for privatlivet fordi data ofte samles inn uten at brukerne er klar over det. Dette kan føre til uønskede konsekvenser som tap av kontroll over egne opplysninger.",
    litenTekst:
      "Sensitive persondata som bilder, lokasjonsdata og kontaktinformasjon kan utnyttes av aktører utenfor individets kontroll. Dette kan gi en følelse av sårbarhet og tap av sikkerhet i det digitale landskapet.",
    fordeler:
      "Kan gi bedre, mer personaliserte tjenester. <br /><br />Effektiv tilgang til digitale plattformer og ressurser. <br /><br />Muliggjør målrettet informasjon og opplevelser tilpasset individuelle behov. <br /><br />Fremmer deling og tilkobling i en digitalisert verden. <br /><br />Øker muligheten for innovasjon og teknologisk utvikling.",
    ulemper:
      "Økt risiko for identitetstyveri og økonomisk svindel. <br /><br />Personlig informasjon kan brukes til overvåkning og manipulering. <br /><br />Uønsket deling av private opplysninger på nett. <br /><br />Målrettet reklame og algoritmestyrt påvirkning av adferd. <br /><br />Kan føre til overavhengighet av digitale systemer.",
    videoTekst:
      "Lovgivning som GDPR har gitt individer mer kontroll over hvordan data behandles. Dette skaper et grunnlag for å balansere personvern med de potensielle fordelene et digitalt fotavtrykk kan tilby. Likevel er det viktig med kontinuerlig bevissthet rundt egne digitale spor.<br><br>Samtidig er det essensielt å forstå hvordan dataene dine kan bli brukt av ulike aktører. Med økt digitalisering er ansvaret for databeskyttelse delt mellom individet og samfunnet. Ved å kombinere bevissthet og riktige verktøy kan vi minimere risikoene og samtidig utnytte de mange fordelene ved et digitalisert liv.",
  },
  engelsk: {
    tittel:
      "Does a large digital footprint affect individual privacy, and does it pose risks?",
    innhold:
      "A large digital footprint may pose a risk to privacy as data is often collected without users being aware. This can lead to unwanted consequences, such as a loss of control over personal information.",
    litenTekst:
      "Sensitive personal data such as photos, location data, and contact information can be exploited by actors outside the individual's control. This can lead to a sense of vulnerability and loss of security in the digital landscape.",
    fordeler:
      "Can provide better, more personalized services. <br /><br /> Efficient access to digital platforms and resources. <br /><br /> Enables targeted information and experiences tailored to individual needs. <br /><br /> Promotes sharing and connectivity in a digitized world. <br /><br /> Increases opportunities for innovation and technological development.",
    ulemper:
      "Increased risk of identity theft and financial fraud. <br /><br /> Personal information can be used for surveillance and manipulation. <br /><br /> Unwanted sharing of private information online. <br /><br /> Targeted advertising and algorithm-driven behavior influence. <br /><br /> May lead to overdependence on digital systems.",
    videoTekst:
      "Legislation such as GDPR has given individuals more control over how data is processed. This creates a foundation for balancing privacy with the potential benefits a digital footprint can offer. However, it is important to maintain continuous awareness of one's digital traces.<br><br>At the same time, it is essential to understand how your data may be used by various actors. With increased digitization, the responsibility for data protection is shared between individuals and society. By combining awareness and the right tools, we can minimize risks while leveraging the many benefits of a digitized life.",
  },
  spansk: {
    tittel:
      "¿Afecta una gran huella digital a la privacidad de las personas y plantea riesgos?",
    innhold:
      "Una gran huella digital puede representar un riesgo para la privacidad, ya que a menudo se recopilan datos sin que los usuarios sean conscientes. Esto puede llevar a consecuencias no deseadas, como la pérdida de control sobre la información personal.",
    litenTekst:
      "Los datos personales sensibles como fotos, datos de ubicación e información de contacto pueden ser explotados por actores fuera del control del individuo.",
    fordeler:
      "Puede proporcionar mejores y más personalizados servicios. <br /><br /> Acceso eficiente a plataformas y recursos digitales. <br /><br /> Permite información dirigida y experiencias adaptadas a las necesidades individuales. <br /><br /> Fomenta la conexión y el intercambio en un mundo digitalizado. <br /><br /> Aumenta las oportunidades de innovación y desarrollo tecnológico.",
    ulemper:
      "Mayor riesgo de robo de identidad y fraude financiero. <br /><br /> La información personal puede ser utilizada para vigilancia y manipulación. <br /><br /> Compartir información privada no deseada en línea. <br /><br /> Publicidad dirigida y algoritmos que influyen en el comportamiento. <br /><br /> Puede conducir a una dependencia excesiva de los sistemas digitales.",
    videoTekst:
      "La legislación como el GDPR ha dado a las personas más control sobre cómo se procesan los datos. Esto crea una base para equilibrar la privacidad con los posibles beneficios que puede ofrecer una huella digital. Sin embargo, es importante mantener una conciencia continua sobre las propias huellas digitales.<br><br>Al mismo tiempo, es esencial comprender cómo pueden ser utilizados tus datos por diversos actores. Con una mayor digitalización, la responsabilidad de la protección de datos se comparte entre los individuos y la sociedad. Al combinar conciencia y las herramientas adecuadas, podemos minimizar los riesgos y aprovechar los muchos beneficios de una vida digitalizada.",
  },
};

function endreSpråk(språk) {
  document.getElementById("tittel").innerHTML = språkData[språk].tittel;
  document.getElementById("innhold").innerHTML = språkData[språk].innhold;
  document.getElementById("liten-tekst").innerHTML =
    språkData[språk].litenTekst;
  document.getElementById("fordeler").innerHTML = språkData[språk].fordeler;
  document.getElementById("ulemper").innerHTML = språkData[språk].ulemper;
  document.getElementById("video-tekst").innerHTML =
    språkData[språk].videoTekst;
}
