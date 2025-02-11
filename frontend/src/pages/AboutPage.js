import React from 'react';
import './gen-page.css';

const AboutPage = () => {
  return (
    <div className="about-container">
      <section>
        <h1>About Calibra</h1>
        <p id='disclaim'>This is a template I made for a personal project, and I have decided to use the same template for an assignment for school, So if you are seeing this that is what this is.</p>
        <p>This template was built on a DRF API, a postgres database, and using React for the frontend.</p>
        <p>Calibra is an all-in-one AI integrated content management and conferencing platform that helps you strwamline the workflow of your business. From managing your data, generating SQL queries, writing reports and so much more.</p>
      </section>

      <section>
        <h2>Our Mission</h2>
        <p>Our mission is to provide businesses with a platform that helps them manage their data, generate reports and streamline their workflow in a more efficient manner, ultimately boosting their productivity and generating a more appealing bottom line.</p>
      </section>

      <section>
        <h2>Our Team</h2>
        <p>Our team is made up of a group of dedicated individuals with a passion for technology and the drive to make a difference in the world of business.</p>
      </section>

      <section>
        <h2>Our Vision</h2>
        <p>Our vision is to provide businesses with a platform that is easy to use, efficient and cost-effective, ultimately helping them to grow and succeed in the ever-evolving world of business.</p>
      </section>
    </div>
  );
}

export default AboutPage;
