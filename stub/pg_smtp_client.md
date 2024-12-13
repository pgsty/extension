
--------

## Usage

> https://github.com/frectonz/pglite-fusion/blob/main/README.md

### Enabling the extension

Connect to postgres and run the following command.

```sql
CREATE EXTENSION IF NOT EXISTS pg_smtp_client CASCADE;
```

## Usage

Use the `smtp_client.send_email()` function to send an email.

### Function Parameters

| Parameter     | Type    | Description                                           | System Configuration (Optional) |
|---------------|---------|-------------------------------------------------------|---------------------------------|
| subject       | text    | The subject of the email                              |                                 |
| body          | text    | The body of the email                                 |                                 |
| html          | boolean | Whether the body is HTML (true) or plain text (false) |                                 |
| from_address  | text    | The from email address                                | `smtp_client.from_address`      |
| recipients    | text[]  | The email addresses of the recipients                 |                                 |
| ccs           | text[]  | The email addresses to CCs                            |                                 |
| bccs          | text[]  | The email addresses to BCCs                           |                                 |
| smtp_server   | text    | The SMTP server to use                                | `smtp_client.server`            |
| smtp_port     | integer | The port of the SMTP server                           | `smtp_client.port`              |
| smtp_tls      | boolean | Whether to use TLS                                    | `smtp_client.tls`               |
| smtp_username | text    | The username for the SMTP server                      | `smtp_client.username`          |
| smtp_password | text    | The password for the SMTP server                      | `smtp_client.password`          |

### Default Configuration

You can configure the following system-wide default values for some of the parameters (as indiciated in the table above) like this:

```
ALTER SYSTEM SET smtp_client.server TO 'smtp.example.com';
ALTER SYSTEM SET smtp_client.port TO 587;
ALTER SYSTEM SET smtp_client.tls TO true;
ALTER SYSTEM SET smtp_client.username TO 'MySmtpUsername';
ALTER SYSTEM SET smtp_client.password TO 'MySmtpPassword';
ALTER SYSTEM SET smtp_client.from_address TO 'from@example.com';
SELECT pg_reload_conf();
```

### Usage Examples

Send an email:
```sql
SELECT smtp_client.send_email('test subject', 'test body', false, 'from@example.com', array['to@example.com'], null, null, 'smtp.example.com', 587, true, 'username', 'password');
```

Send an email using configured default values:
```sql
SELECT smtp_client.send_email('test subject', 'test body', false, null, array['to@example.com']);
```

Or, using named arguments:
```sql
SELECT smtp_client.send_email('test subject', 'test body', recipients => array['to@example.com']);
```