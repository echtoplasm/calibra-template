import React from 'react';
import './gen-page.css';

const Services = () => {
  return (
    <div className="about-container">
      <section>
        <h1>Our Services</h1>
        <p>Calibra offers a range of services to help you streamline your workflow and boost your productivity. All of our AI integrated services use natural language processing to make it as seamless as possible for your team to interact with the services.</p>
      </section>

        <section>
          <h2>Try Our Demo</h2>
          <p>Try our demo to see how our AI integrated services can help you streamline your workflow and boost your productivity.</p>
          <button onClick={() => window.location.href='/demo'}>Demo</button>
        </section>

      <section>
        <h2>AI Integrated Conferencing</h2>
        <p>Our AI integrated conferencing platform allows you to seamlessly transcribe meeting details, generate SQL queries, draft and send emails, set reminders and much more, all without any interruption to the workflow.</p>
      </section>

      <section>
        <h2>Data Management</h2>
        <p>Our data management services help you manage your data more efficiently, generate reports, visualize data and more.</p>
      </section>

      <section>
        <h2>Database, Spreadsheet, Word Document Integration</h2>
        <p>Our platform integrates with databases, spreadsheets and word documents to help you manage your data more effectively, as well automate tasks in these areas, such as generating SQL queries, writing reports, and automating spreadsheet data entry.</p>
      </section>

      <section>
        <h2>Workflow Automation</h2>
        <p>Our workflow automation services help you automate repetitive tasks, streamline your workflow and boost your productivity.</p>
      </section>

      <section>
        <h2>Custom Solutions</h2>
        <p>Our team of experts can work with you to develop custom solutions to meet your specific needs.</p>
      </section>

      <section>
        <h2>24/7 Support</h2>
        <p>Our team of experts is available 24/7 to provide you with the support you need.</p>
      </section>
    </div>
  );
}

export default Services;
